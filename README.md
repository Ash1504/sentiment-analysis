# sentiment-analysis
Sentiment Analysis of Patient Reviews on Drugs


The project is divided into multiple sections
1. Data Extraction:
For Data Extraction, Python BeautifulSoup library was used to extract patient reviews from the websites links present in the file Review_Links.csv
The extracted data was then saved into a new CSV file for further processing and analysis.

2. PreProcessing:
In this folder, the extracted data is cleaned using different NLP pre processing techniques such as lemmatization, contraction, stop words removal to name a few. The processed data is then stored into a file for sentiment analysis and key phrases extraction.

3. Azure Text Analytics:
For sentiment analysis and key phrases extraction, a new azure account was created and Text Analytics service was set up for which the steps are described in the Setting Up Azure Cognitive Service.docx The sentiment and key phrases of each drugs are stored into a separate file present in the folder Azure.

4. Sentiment Analysis using Python
In this section different vectorizing techniques such as Count Vectorizer and TF-IDF Vectorizer is used and the model is trained with different classic machine learning algorithms such as XGBoost, Support Vector Machine, Random Forest Classifier and Logistics Regression. The performance of each of these models are then compared with Azure Service.

5. Exploratory Data Analysis
EDA has been performed on the sentiment to find out the top and worst performing drugs in the market particulary for Depression. The word cloud for those drugs are alos plotted using Key Phrases that was extracted before using Azure Text Analytics.
