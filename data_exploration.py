# -*- coding: utf-8 -*-
"""Data_Exploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G6N27md5UEcBI8gQlait7QWux5k3DDNm

#Data Exploration part 

This module consists of data pre-processing for the project.

Raw Data for project is already collected (Source: Kaggle)
"""

# library part

import pandas as pd

import numpy as np

from google.colab import files

# loading dataset to IDE as DataFrame

data = pd.read_csv('/Bank Customer Churn Prediction.csv')

data.head()

#Information about dataset

data.info()

#removing unnecessary attributes

data = data.drop('customer_id',axis=1)

#Checking for duplicated values

data.duplicated().sum()

#checking for null(empty entry) values

data.isnull().sum()

data['balance']

#Replacing null values with average(mean) value of the attribute

b_mean = data['balance'].mean()

data['balance'].fillna(b_mean, inplace=True)

data

# changing binary variables of attributes 'credit_card','active_member' and 'churn' to 0 & 1 for easy mathematical purpose 

data['credit_card'] = data['credit_card'].replace(to_replace = ['YES','NO'],value = ['1','0'])

data['active_member'] = data['active_member'].replace(to_replace = ['ACTIVE','NON_ACTIVE'],value = ['1','0'])

data['churn'] = data['churn'].replace(to_replace = ['YES','NO'],value = ['1','0'])

data

data.head(10)

data.tail(10)

#Downloading pre-processed dataframe as csv

data.to_csv('Data_exploration.csv', header=True, index=False)

files.download('Data_exploration.csv')

