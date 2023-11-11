# traffic-prediction-backend

Step 1: Pre Processing

a. import pandas

b. import the csv file

c. remove the unwanted columns - ID

d. convert the datetime column into a datetime object

e. extract hour, month and day to new columns

f. map the days to numbers. [monday to sunday : 1 to 7]

g. extract the week of the month

h. remove datetime col

i. convert the data set to classification dataset

j. We will use the number of vehicles to determine the traffic level

k. Check the max number of vehicles - 180

l. divide the vehicle count 180 into 3 then get the class intervals for the traffic classification

0-30 Low
31-60 Medium
60+ High

m. map the traffic level to integers

n. convert the pre processed data frame to a csv file

================================================================

Step 2: Build the model

a. import the necessary libraries.

b. import the pre processed dataset

c. split the dataset into input and output

d. balance the dataset

e. split to train test data

f. Initialize the random forest classifier

g. tune the hyperparameters, can use grid search csv to find optimum amount of decision trees

h. train the model and the save the trained model using pickle

================================================================

Step 3: Building the flask application

a. importing the libs

b. loading the model

c. building the routes

d. getting the input from the user then using the same preprocessing as we did for the data set

e. predict the value and return through the /predict route




![Random Forest - Confusion Metrix](https://github.com/Manuja100/traffic-prediction-backend/assets/99438342/2540c1cd-785b-426c-a234-c9c815bdacf3)
![Random Forest - Classification Report](https://github.com/Manuja100/traffic-prediction-backend/assets/99438342/03cc0c3b-1ae1-4dc4-8b44-38700ee914d3)


