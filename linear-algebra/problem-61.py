"""
Problem: https://www.deep-ml.com/problem/F-Score%20Calculation

"""

import numpy as np

def f_score(y_true, y_pred, beta):

    TP, TN, FP, FN = 0, 0, 0, 0  # Set initial values for all variables
    
    # calculate TP, TN, FP and FN
    for actual, predicted in zip(y_true, y_pred):
        if actual == 1 and predicted == 1:
            TP += 1
        elif actual == 0 and predicted == 1:
            FP += 1
        elif actual == 1 and predicted == 0:
            FN += 1

    precision = TP / (TP + FP) 
    recall = TP / (TP + FN) 
    b_2 = beta ** 2
    
    fscore = ((1 + b_2) * precision * recall) / (b_2 * precision + recall) 
    return round(fscore,3)

