# Authors:
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

################################################# Import Libraries ###############################################
import numpy as np
import csv
from scipy.sparse import csr_matrix
import pandas as pd
import time
import implicit
from scipy import sparse
from scipy.sparse import coo_matrix
import operator

###################################################################################################################

############################################  Data Pre-processing  ################################################


## Read the data containing the users, businesses and the stars
data = pd.read_csv('model_data.csv')

print "Data pre-processing"
## Data pre-processing
users=list(set(data['user_id'].values))
userdict={}
rev_user_dict ={}
rev_business_dict = {}
for i in range(len(users)):
    userdict[users[i]]=i
    rev_user_dict[i] = users[i]
businessdict={}
businesses=list(set(data['business_id'].values))


for i in range(len(businesses)):
    businessdict[businesses[i]]=i
    rev_business_dict[i] = businesses[i]  
sparseM=np.zeros((len(users), len(businesses)))


for row in data.values:
    sparseM[userdict[row[0]]][businessdict[row[1]]]=row[2]

print "Data pre-processing done"

###################################################################################################################

######################################     Model Training and gining prediction    ############################################
# initialize a model
model = implicit.als.AlternatingLeastSquares(factors=50)

print "The model is training"
# train the model on a sparse matrix of user/business/review stars
model.fit(sparse.csr_matrix(sparseM))

print "Model training is done"


## Asking the user to enter the user to get the recommendations
while(True):
	print "Enter the user_id to get the recommendations for potential friends based on similar interests(Enter values between ", 1," and ", len(users),"): "
	user_id = input()
	if 1 <= int(user_id) <= len(users):
		break
	else:
		print "Please enter correct user_id"	

## Making recommendations for the user_id specified using content based filtering
user = rev_user_dict[user_id]
business_reviewed = data[data["user_id"] == user]["business_id"].values
reccomend_dict = {}
flag = 1
for business in business_reviewed:
	business = businessdict[business]
	related = model.similar_items(business)
	for r in related:
		if flag == 1:
			flag = 0
			continue
		if r[0] not in reccomend_dict:
			reccomend_dict[r[0]] = r[1]
		else:
			reccomend_dict[r[0]] += r[1]

sorted_dict = sorted(reccomend_dict.items(), key=operator.itemgetter(1))
print "Following are the potential list of users recommended for the given user to be friends with: "
count = 0
for i in sorted_dict:
	if count <= 10:
		print i[0]
		count += 1

###################################################################################################################