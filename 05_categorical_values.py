# libraries

import pandas as pd
import numpy as np

veriler= pd.read_csv('eksikveriler.csv')


print(f'eksik veriler: \n {veriler}')


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

print('Label encoding oncesi')
print(ulke)

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print('Label encoding sonrasi')
print(ulke)
