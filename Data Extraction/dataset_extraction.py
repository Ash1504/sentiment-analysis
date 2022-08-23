import pandas as pd
import requests
from bs4 import BeautifulSoup

# read the review links file
root = r"C:\Users\ashis\OneDrive\Desktop\UL\Dissertation\\"
file_path = root+"Review_Links.csv"
df = pd.read_csv(file_path)

# new dataframe to fetch details from links
new_df = pd.DataFrame(columns='Drug_Name,Patient_Review,Ratings,Condition,Dosage,Other_conditions,Other_drugs_taken,Benefits,Side_effects,Comments'.split(','))

# code for fetching details from webpage
for index, rows in df.iterrows():
    url = rows["Review URL"]
    drug = rows["Drug"]
    print(" Processing for drug: {}".format(drug))
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for h2 in soup.select("h2"):
        # patient review
        pr = h2.text

        # ratings
        ratings = len(
            h2.find_next(class_="review3").find_all(
                lambda tag: tag.name == "img" and "red_star" in tag.get("src", "")
            )
        )
        # conditions
        condition = h2.find_next(lambda tag: tag.name == "td" and "Condition / reason:" in tag.text).find_next("td").find_next(class_="review3").text
        
        # dosage
        dosage = h2.find_next(lambda tag: tag.name == "td" and "Dosage & duration:" in tag.text).find_next("td").find_next(class_="review3").text

        # other conditions
        Other_conditions = h2.find_next(lambda tag: tag.name == "td" and "Other conditions:" in tag.text).find_next("td").find_next(class_="review3").text
        
        # other drugs taken
        other_drugs_taken = h2.find_next(lambda tag: tag.name == "td" and "Other drugs taken:" in tag.text).find_next("td").find_next(class_="review3").text
        
        # benefits
        benefits = h2.find_next("td", text="Benefits:").find_next(class_="review3").text
        
        # side effects
        side_effects = (
            h2.find_next(lambda tag: tag.name == "td" and "Reported Results" in tag.text)
            .find_next("td", text="Side effects:")
            .find_next(class_="review3")
            .text
        )
        # comments
        comments = h2.find_next("td", text="Comments:").find_next(class_="review3").text
        
        
        series = pd.Series([drug, pr, ratings,condition,dosage,Other_conditions,other_drugs_taken, benefits, side_effects, comments], index = new_df.columns)
        new_df = new_df.append(series, ignore_index=True)
    
# pre-processing

# 1. Drop Duplicates
new_df.drop_duplicates(keep='first',inplace=True)

# 2. Preprocessing string data
new_df.loc[:,"Drug_Name"] = new_df.loc[:,"Drug_Name"].str.lower().str.strip()
new_df.loc[:,"Patient_Review"] = new_df.loc[:,"Patient_Review"].str.lower().str.strip()
new_df.loc[:,"Condition"] = new_df.loc[:,"Condition"].str.lower().str.strip()
new_df.loc[:,"Dosage"] = new_df.loc[:,"Dosage"].str.lower().str.strip()
new_df.loc[:,"Benefits"] = new_df.loc[:,"Benefits"].str.lower().str.strip()
new_df.loc[:,"Side_effects"] = new_df.loc[:,"Side_effects"].str.lower().str.strip()
new_df.loc[:,"Comments"] = new_df.loc[:,"Comments"].str.lower().str.strip()
new_df.loc[:,"Other_conditions"] = new_df.loc[:,"Other_conditions"].str.lower().str.strip()
new_df.loc[:,"Other_drugs_taken"] = new_df.loc[:,"Other_drugs_taken"].str.lower().str.strip()

# 3. Replace unwanted values and fill na values and load to csv
new_df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r","none","nil","n/a","na"], value=["","","","","",""], regex=True, inplace=True)
new_df.fillna("",inplace=True)
new_df.to_csv(root+"extracted_data.csv",index=False)
