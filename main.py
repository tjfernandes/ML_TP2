#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:58:00 2023

@author: Tiago Fernandes 57677, Francisco Silva 

Multiple myeloma survival

This program generates a model which predicts the survival time of the cancer patients

"""

<<<<<<< HEAD
=======
import pandas as pd


# Open train and test sets as dataframes 
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

print("First few rows:")
print(train_data.head())

print("\nData Summary:")
print(train_data.info())

print("\nDescriptive Statistics:")
print(train_data.describe())

print("\nNumber of Rows and Columns:")
print(train_data.shape)
>>>>>>> c701a49 (added txt with set information)
