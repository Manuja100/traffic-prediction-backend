import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle

#import the preprocessed dataset  file
trafficData = pd.read_csv('datasets/traffic_preprocessed.csv')