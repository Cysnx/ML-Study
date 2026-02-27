# libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler= pd.read_csv('veriler.csv')

print(f'Veriler: \n {veriler}')


boy_kilo_yas=veriler.iloc[:,1:4]

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

#ülkelerin dönüşmeleri
ulke = le.fit_transform(veriler.iloc[:,0])
ulke = ulke.reshape(-1,1)

print(ulke)

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

#cinsiyet dönüşümleri
cinsiyet = le.fit_transform(veriler.iloc[:,-1])
cinsiyet = cinsiyet.reshape(-1,1)

print(cinsiyet)

ohe=preprocessing.OneHotEncoder()
cinsiyet=ohe.fit_transform(cinsiyet).toarray()
print(cinsiyet)


#merging
print(list(range(22)))

""" encode ettiğim 'ülke' verilerini 0'dan başlayıp 21'e kadar yani 'index'=22 olacak şekilde
ve veri başlıkları da ülke isimleri olacak şekilde bir sonuc dataframe'i oluştur """

sonuc=pd.DataFrame(data=ulke, index = range(22), columns=['fr','tr','us'])
print("Encode edilmiş ülkeler, DATAFRAME olarak:")
print(sonuc)

# yas diye adlandırmısız ama aslında sayısal veriler.
sonuc2=pd.DataFrame(data=boy_kilo_yas, index=range(22), columns=['boy','kilo','yas'])
print("Encode edilmiş boy kilo ve yaş, DATAFRAME olarak:")
print(sonuc2)

sonuc3=pd.DataFrame(data=cinsiyet[:,0:1], index=range(22), columns=['cinsiyet']) # dummy varible dikkat!
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

x_train, x_test, y_train, y_test=train_test_split(s,sonuc3,test_size=0.33, random_state=0)

# Model Construction - Cinsiyet tahmin etmece

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred=regressor.predict(x_test) # tahmin

# Model Construction - boy tahmin etmece
## verinin oluşturulması
boy=s2.iloc[:,3:4].values
print(boy)

sol=s2.iloc[:,:3]
sag=s2.iloc[:,4:]

veri=pd.concat([sol,sag], axis=1)

x_train, x_test, y_train, y_test=train_test_split(veri,boy,test_size=0.33, random_state=0) # verinin test/train yapısında bölünmesi

r2 = LinearRegression()
r2.fit(x_train, y_train)

y_pred=regressor.predict(x_test) # tahmin
