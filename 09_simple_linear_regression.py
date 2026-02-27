# libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler= pd.read_csv('satislar.csv')


print(f'eksik veriler: \n {veriler}')

aylar=veriler[['Aylar']]
print('Aylar: \n',aylar)

satislar=veriler[['Satislar']]
print('Satislar: \n ',satislar)
"""
satislar2=veriler.iloc[:,:1].values
print(satislar2)"""

print(veriler)
# Train_Test_Split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(aylar,satislar,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)