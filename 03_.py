# libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler= pd.read_csv('eksikveriler.csv')


print(f'eksik veriler: \n {veriler}')

boy=veriler[['boy']]
print('boy: \n',boy)

boykilo=veriler[['boy','kilo']]
print('boykilo: \n ',boykilo)

class insan:
    boy=180
    def kosmak(self,b):
        return b+10
    # y= f(x)
    # f(x) = x+10

ali=insan()
print(ali.boy)
print(ali.kosmak(90))

#missing values

from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
yas=veriler.iloc[:,1:4].values
print(yas)
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])
print(yas)


