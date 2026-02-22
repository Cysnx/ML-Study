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
yas=veriler.iloc[:,1:4].values ### BIRINCI ve DORDUNCU SUTUNLAR ARASINDAKI VERILER (1,2,3 -- 0 ve 4 yok)
print("Printing iloc 1-4... which means columns 1 2 3")
print(yas)
imputer=imputer.fit(yas[:,1:4]) # impute edilecek nan verileri belirle.

yas[:,1:4]=imputer.transform(yas[:,1:4]) # impute'u imputer stratejisine göre veriye geçir.
print(yas)

ulke= veriler.iloc[:,0:1].values
print(ulke)

# catogeric values to ordinal values, conversion. #encoding

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
ulke = le.fit_transform(veriler.iloc[:,0])
ulke = ulke.reshape(-1,1)

print(ulke)

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)
