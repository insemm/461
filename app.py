import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

test_data = pd.read_csv("test_data.csv")
train_data = pd.read_csv("train_data.csv")

#choose train
train_x = train_data.drop(columns=['category'],axis=94)
train_y = train_data['category']

#xgboost
model = XGBClassifier( learning_rate =0.1)
model.fit(train_x, train_y)

predict_train = model.predict(train_x)
print('\nTarget on train data',predict_train) 

accuracy_train = accuracy_score(train_y,predict_train)
print('\naccuracy_score on train dataset : ', accuracy_train)

predict_test = model.predict(test_data)

df = pd.DataFrame(predict_test)

with open('file2.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["key","group_01","group_02","group_03","group_04","group_05","group_06","group_07","group_08","group_09"])

with open('file2.csv', 'a', newline='') as fd:
    writer = csv.writer(fd)
    for i in range(df.shape[0]):
        if df.iloc[i,0] == "Class_1":
            writer.writerow([test_data.iloc[i,0],"1","0","0","0","0","0","0","0","0"])
        elif df.iloc[i,0] == "Class_2":
            writer.writerow([test_data.iloc[i,0],"0","1","0","0","0","0","0","0","0"])
        elif df.iloc[i,0] == "Class_3":
            writer.writerow([test_data.iloc[i,0],"0","0","1","0","0","0","0","0","0"])
        elif df.iloc[i,0] == "Class_4":
            writer.writerow([test_data.iloc[i,0],"0","0","0","1","0","0","0","0","0"])
        elif df.iloc[i,0] == "Class_5":
            writer.writerow([test_data.iloc[i,0],"0","0","0","0","1","0","0","0","0"])
        elif df.iloc[i,0] == "Class_6":
            writer.writerow([test_data.iloc[i,0],"0","0","0","0","0","1","0","0","0"])
        elif df.iloc[i,0] == "Class_7":
            writer.writerow([test_data.iloc[i,0],"0","0","0","0","0","0","1","0","0"])
        elif df.iloc[i,0] == "Class_8":
            writer.writerow([test_data.iloc[i,0],"0","0","0","0","0","0","0","1","0"])
        else:
            writer.writerow([test_data.iloc[i,0],"0","0","0","0","0","0","0","0","1"])