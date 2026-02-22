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

# catogeric values to ordinal values, conversion.

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
ulke = le.fit_transform(veriler.iloc[:,0])
ulke = ulke.reshape(-1,1)

print(ulke)
     ### One hot encoder - OHE, verileri 1 0 0, 010, 001 gibi (sütun sayısına göre değişecek) dönüştürme
ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

#merging
print(list(range(22)))

""" encode ettiğim 'ülke' verilerini 0'dan başlayıp 21'e kadar yani 'index'=22 olacak şekilde
ve veri başlıkları da ülke isimleri olacak şekilde bir sonuc dataframe'i oluştur """

sonuc=pd.DataFrame(data=ulke, index = range(22), columns=['fr','tr','us'])
print("Encode edilmiş ülkeler, DATAFRAME olarak:")
print(sonuc)

# yas diye adlandırmısız ama aslında sayısal veriler.
sonuc2=pd.DataFrame(data=yas, index=range(22), columns=['boy','kilo','yas'])
print("Encode edilmiş boy kilo ve yaş, DATAFRAME olarak:")
print(sonuc2)

cinsiyet=veriler.iloc[:,-1].values # cinsiyet
print("cinsiyet, LISTE olarak:")
print(cinsiyet)

sonuc3=pd.DataFrame(data=cinsiyet, index=range(22), columns=['cinsiyet'])
print("cinsiyet, DATAFRAME olarak:")
print(sonuc3)

""" birleştirmelerin başladığı yer"""

s=pd.concat([sonuc,sonuc2],axis=1)
print("Encode edilmiş ülkeler ve boy-kilo-yaş, DATAFRAME olarak:")
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print("Encode edilmiş ülkeler, boy-kilo-yaş ve cinsiyet, DATAFRAME olarak:")
print(s2)

# Train_Test_Split

from sklearn.model_selection import train_test_split

# verilerin train ve test diye ayrılması
x_train, x_test, y_train, y_test=train_test_split(s,sonuc3,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

# verilerin train ve test diye ayrılması
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)