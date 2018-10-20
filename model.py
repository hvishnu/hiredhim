import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from frontendhire import *

df = pd.read_csv('prepdata.csv')

X = df[['PERCENTAGE', 'BACKLOG', 'INTERNSHIP', 'FIRSTROUND','COMMUNICATIONSKILLLS']]
y = df['Hired']

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=20)

from sklearn import svm, datasets
C = 1.0
svc = svm.SVC(kernel='sigmoid', C=C).fit(X, y)

lr.fit(X,y)
dt.fit(X,y)
rf.fit(X,y)
svc.fit(X,y)

def logistic(percent,backlog,internship,firstRound,communicationSkill):
    global pred,X_test
    X_test = [[percent,backlog,internship,firstRound,communicationSkill]]
    pred = lr.predict(X_test)
    return pred

def decisionTree(percent,backlog,internship,firstRound,communicationSkill):
    global pred
    pred = dt.predict([[percent,backlog,internship,firstRound,communicationSkill]])
    return pred

def randomForest(percent,backlog,internship,firstRound,communicationSkill):
    global pred
    pred = rf.predict([[percent,backlog,internship,firstRound,communicationSkill]])
    return pred

def svm(percent,backlog,internship,firstRound,communicationSkill):
    global pred
    pred = svc.predict([[percent,backlog,internship,firstRound,communicationSkill]])
    return pred