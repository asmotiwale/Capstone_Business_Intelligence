# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa
################### Code to extract the review data for the state of North Carolina ################

import pandas as pd
import numpy as np


## Extracting business_id of businesses in North Carolina 

df = pd.read_csv("businessGrouped.csv", sep = ",")
# print business_id
df_nc = df[df['state'] == 'NC']
business = df_nc['business_id']
business_id = business.values
# business.to_csv("review_nc.csv", sep = ",")
# print business_id[0]
review_nc = pd.DataFrame()

df = pd.read_csv("review.csv", sep = ",")
count = 0
for i in business_id:
	count += 1
	print count
	print i
	review_nc = review_nc.append(df[df['business_id'] == i])	
review_nc.to_csv("review_nc.csv", sep = ",")