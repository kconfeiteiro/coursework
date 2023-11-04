# %% [markdown]
# # Assignment 4
# | Topic | Information |
# | --------  |  -------- |
# | Team Members | Antonio Cascio & Krystian Confeiteiro |
# | Professor    | Dr. Jack |
# | Course       | DS 440 - 01DB |
# | Assignment   | Assignment 5 |
# | Date         | 10/05/2023 |
#
# ## Assignment Objective
# Use the car evaulation dataset below, suppose you want to develop a machine learning model to predict the values in the last column, develop your own function to calculate:
# 1. The entropy of the original dataset when there is no split.
# 2. The information gains on choosing each attribute to split the dataset.
#
# Hint: We don't need to construct the complete decision tree in this assignment, please just compute the information gain of the first level split using each attribute (column).
# # Assignment Layout
#
# # Assignment Checklist
# Submission:
#
# - Link to your Colab notebook via comment function
# - `.ipynb` file as required by record office.

# %%
from math import log

import numpy as np
import pandas as pd
from sklearn.tree import *

DATA = pd.read_csv("CarEval.csv")
print("Data columns: ", DATA.columns)
print(DATA.head(), "\n\n")


# define function to calcualte entropy
def calc_entropy(column):
    column = []
    counts = np.bincount(column)
    probability = counts / (len(column))

    return -sum((-prob * log(prob, 2)) if prob > 0 else 0 for prob in probability)


def information_gain(data, attr_index, col):
    # calculate total entropy
    entropy_total = calc_entropy(col)

    # pull column values and counts using numpy
    col_data = data[data.columns[attr_index]]
    attr_values, counts = np.unique(col_data, return_counts=True)

    # calculate weighted entropy
    entropy_weighted = 0
    for value, count in zip(attr_values, counts):
        col_data_w = data[data.iloc[:, attr_index] == value]
        calcd_entropy = calc_entropy(col_data_w)
        entropy_weighted += (count / len(data)) * calcd_entropy

    info_gain = entropy_total - entropy_weighted
    return info_gain


col_indx = -3
info_gain_calc = information_gain(DATA, col_indx, DATA[DATA.columns[col_indx]])
entropy_calc = calc_entropy(DATA[DATA.columns[col_indx]])

print("Calculated entropy: ", entropy_calc)
print("Calculated information gain: ", info_gain_calc)
