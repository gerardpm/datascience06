# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:57:19 2015

@author: gerar_000
"""

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
df = pd.read_csv('C:\\Users\\gerar_000\\Projects\\SampleData.csv')

df.head()

dfTrain, dfTest = train_test_split(df, test_size=0.2)

cl = dfTrain[:,2]

dfTest[:,2]