# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa
#CODE TO COMPUTE TOP 15 FREQUENT WORDS IN REVIEWS CORPUS

import pandas as pd
import numpy as np
from random import shuffle
import os
import sys
import json
import csv
import ast
import re
from collections import Counter
import nltk
from string import punctuation
import sklearn.feature_extraction.text
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt



def content_text(text):
    additionalstopwords=["i","it's","the","go","back","got","just","year","really","totally","year","week","","place","I'd","if"]  
    stopwords = set(sklearn.feature_extraction.text.ENGLISH_STOP_WORDS.union(additionalstopwords))          #add additional stopwords to existing ones
    without_stp  = Counter()                                                                                #initialize counter

    for line in text.splitlines():                                                                          #for each line in corpus
        spl = line.split()                                                                                  #split the line into words
        for w in spl:                                                                                       #for each word in line
            word=w.lower().rstrip(punctuation)                                                              #make lower case and remove punctuations    
            if word not in stopwords:
                without_stp[word]+=1                                                                        #if the word is not in stopword increment its counter
    return [y for y in without_stp.most_common(15)]


def main():
 
    reviews=pd.read_csv('.\\yelp dataset\\review.csv')                                                      #read the review dataset
    
    for fl in os.listdir(".\\yelp dataset\\NC\\"):                                                          #for each file in NC folder
        path=os.path.join(".\\yelp dataset\\NC\\",fl)   
        trendDF=pd.read_csv(path)                                                                           #read the trend data into trendDF
        trendDF['FrequentWords']=''
        for index, row in trendDF.iterrows():
            bid=row[0]                                                                                      #extract all the reviews for given business ID and merge to form a string
            text=(reviews[reviews['business_id']==bid]['text'].str.cat(sep=' '))
            wthout_stop = str(content_text(text))
            trendDF.set_value(index,'FrequentWords',wthout_stop)
        trendDF=trendDF[[1,3,4]]                                                                            #update the dataframe
        trendDF.columns = ['Name', 'Type','FrequentWord']                               
        trendDF.to_csv(path, sep=',')                                                                       #write updated DF to csv
            


    
if __name__ == "__main__":
    main()
