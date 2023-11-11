import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle

#import the preprocessed dataset  file
df = pd.read_csv('datasets/traffic_preprocessed.csv')

#split to input and output
x = df.drop('Traffic_Level', axis = 1)
y = df['Traffic_Level']

#using SMOTEEN to balance the data
#it is a mix of over-sampling and under-sampling
from imblearn.combine import SMOTEENN
smote = SMOTEENN(random_state=42)
x_smoteen, y_smoteen = smote.fit_resample(x, y)

#split to train and test data
X_train, X_test, y_train, y_test = train_test_split(x_smoteen, y_smoteen, test_size = 0.2, shuffle = True)

#training the random forest classifier by tuning hyperparameters
random_forest = RandomForestClassifier(n_estimators=15, max_features = 'log2', max_depth = 15)
random_forest.fit(X_train, y_train)

#save the model for future use
pickle.dump(random_forest, open('model.pkl', 'wb'))