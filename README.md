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

b.
