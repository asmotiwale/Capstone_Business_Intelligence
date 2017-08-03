# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

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

def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

def flattenjson( b ):
    val = {}
    #print(b)
    for i in b.keys():
            if isinstance(b[i], basestring):
                val[i] = b[i].encode('utf8')
            else:
                val[i] = b[i]
    return val


def main():

    #read json data and write to csv files
    '''
    data = []
    with open('yelp_academic_dataset_user.json') as data_file:
        for line in data_file:
             data.append(json.loads(line))

    data = map( lambda x: flattenjson( x ), data )
    columns = [ x for row in data for x in row.keys() ]
    columns = list( set( columns ) )

    with open( 'user.csv', 'wb' ) as out_file:
        csv_w = csv.writer( out_file )
        csv_w.writerow( columns )
        for i_r in data:
            csv_w.writerow( map( lambda x: i_r.get(x), columns ) )
    
    
    
    businessDF=pd.read_csv('business.csv')
    
    #Extract all the categories with which businesses are tagged
    
    categories= businessDF['categories'].dropna()
    flatten = lambda l: ast.literal_eval(l)
    categories=categories.map(flatten)
    l=[]
    map(l.extend, categories)
    print(len(l))
    l=pd.DataFrame(list(set(l)))
    l.to_csv('categories.csv', sep=',')
    '''

    #Manually assign each category a broader business category like Food services, Medical services
    
    #Assign each business a broad category based on majority among the business category of associated category tags
    '''
    businessDF=businessDF.dropna(subset=['categories'])
    df=pd.read_csv('categories.csv').values
    catDict={}
    for i in range(len(df)):
        catDict[df[i][0]]=df[i][1]
        
    categories= businessDF['categories']
    flatten = lambda l: ast.literal_eval(l)
    categories=categories.map(flatten)
    for l in categories:
        for i in range(len(l)):
            l[i]=catDict[l[i]]

    categories = categories.map(lambda x: Most_Common(x))
    businessDF['businesscategory']=categories
    businessDF.to_csv('businessGrouped.csv', sep=',')
    '''

    #read check in data from yelp dataset and club the data day wise i.e #of checkins on monday, #of checkins on tuesday,....... This data will form the basis our TS
    '''
    checkinDF=pd.read_csv('C:\\Miniconda2\\yelp dataset\\checkin.csv')
    days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in range(len(checkinDF)):  
        t=checkinDF['time'][i]
        checkinlist=[]
        for day in days:
            match=re.findall(day+'-\d+:(\d+)', t)
            match=map(int,match)
            checkinlist.append(sum(match))

        checkinDF['time'][i]=checkinlist

    checkinDF.to_csv('CheckinDaywise.csv',sep= ',')
    '''
    

    
if __name__ == "__main__":
    main()
