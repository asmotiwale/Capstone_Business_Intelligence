# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

import pandas as pd
from collections import Counter
import nltk
from string import punctuation
import sklearn.feature_extraction.text
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def main():

    trendDF=pd.read_csv('.\\NC\\NC_trend_Belmont.csv')
    for index, row in trendDF.iterrows():
        wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=1200,height=1000).generate(row[3])
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
    
  
if __name__ == "__main__":
    main()
