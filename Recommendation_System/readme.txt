Team members:
1. Anuraag Motiwale - asmotiwa
2. Abhishek Singh - aksingh5
3. Parag Nakhwa - psnakhwa


This the Readme file for the content based reccomender system implemented in this project.

Description for files in the folder:
1. pre-processing-1.py - 
	This file has the code for data pre-processing. The code extracts the reviews for businesses present in the North Carolina region from the entire review data set.
	We have decided to use North Carolina state for the purpose of scalability. This code can be changed to include other states just by changing the name of the state on line 11. This code writes the output as review_nc.csv in the current folder.

2. pre-processing-2.py - 	
	This file is also used for data pre-processing. This code creates a new csv file as model_data.csv which contains the mapping of the user_id, business_id and the stars given by the user to that business.

3. businessGrouped.csv - 
	This file contains all the businesses categorized into the 34 broad categories based on their category tags given.

4. review_nc.csv - 
	This csv file contains all th reviews given for the businesses present in the North Carolina state by the users.

5. model_data.csv - 
	This csv file contains the mapping of user_id, business_id and the respective strs given by the user to that business.

6. reccommend.py - 
	This file contains the code for making predictions for a user about the potential friends that he/she can find based on similar interest.


Libraries used: 
1. numpy
2. scipy
3. implicit
4. csv
5. pandas
6. operator
7. time

Use "pip install <Library-Name>" toinstall the above libraries.

Steps to run the program:
No need to run the data pre-processing files as pre-processed data is already present in the folder.
Data to be used - model_data.csv
1. Install the libraries mentioned above.
2. Simply run the python file reccommender.py as - "python reccommend.py".
3. The program runs and builds the model and will ask the user about the user id for which he.she wants the reccommendations for friends based on similar interests.
4. The program exits after giving the top 10 friends suggestion for the given user id.