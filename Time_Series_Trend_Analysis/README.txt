# Team Members:
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

Data Required: The file “review.csv” is required to run the program. Since, this file is large in memory, please get the review.csv file from the Time_Series_Trend_Analysis folder using this link - https://drive.google.com/open?id=0B6jireOVa3MkRmc3UWI0QlFCTTA

Libraries used: Pandas, Numpy, sklearn, re, wordcloud, matplotlib. Install using pip install X command.

Steps for runing the program:

1) Place business.csv, categories.csv, checkin.csv, review.csv, tip.csv, user.csv, businessGrouped.csv, and CheckinDaywise.csv provided as part of dataset with this project in the root directory.

###
Kindly ignore the preprocessing.py file, its contains basic groundwork to preprocess the existing datasets and to create new datasets which would serve as pivots later in our code.

Datasets before preprocessing : yelp_academic_dataset_business, yelp_academic_dataset_checkin, yelp_academic_dataset_review, yelp_academic_dataset_tip and yelp_academic_dataset_user

Datasets obtained after preprocessing: business.csv, categories.csv, checkin.csv, review.csv, tip.csv, user.csv, businessGrouped.csv, and CheckinDaywise.csv
###

2) Set the working directory to current root directory where all the preprocessed datasets are palced in R.

3) Run timeSeriesAnalysis.R.

4) Run postprocessing.py.

5) Find the city-wise data for trending businesses grouped by requested business category in NC folder in current root directory. 

6) Run wcloud.py for required city if needed.