# libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler= pd.read_csv('veriler.csv')
print("\n Veriler \n")
print(veriler)


boy_kilo_yas=veriler.iloc[:,1:4]

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

#ülkelerin dönüşmeleri
ulke = le.fit_transform(veriler.iloc[:,0])
ulke = ulke.reshape(-1,1)
print("\n Ülkeler \n")
print(ulke)

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print("\n Encoded - Ülkeler \n")
print(ulke)

#cinsiyet dönüşümleri
cinsiyet_ft = le.fit_transform(veriler.iloc[:,-1])
cinsiyet_ft = cinsiyet_ft.reshape(-1,1)
print("\n Transofmed - Cinsiyetler \n")
print(cinsiyet_ft)


#Dummy variable için yazılmış. 
#Aynı anda hem E/K hem de encoded versiyonu olmamalı..
#Öyle şekilde atılmalı ki son kalan kolondan yeterli çıkarım yapılabilmeli.
ohe=preprocessing.OneHotEncoder()
cinsiyet=veriler.iloc[:,-1:].values
cinsiyet=ohe.fit_transform(cinsiyet).toarray()
print("\n Encoded - Cinsiyetler - DUMMY VARIABLE / KUKLA DEGISKEN \n")
print(cinsiyet)


#merging
print("\nRange'i anlamak\n")
print(list(range(22)))

""" encode ettiğim 'ülke' verilerini 0'dan başlayıp 21'e kadar yani 'index'=22 olacak şekilde
ve veri başlıkları da ülke isimleri olacak şekilde bir sonuc dataframe'i oluştur """

sonuc=pd.DataFrame(data=ulke, index = range(22), columns=['fr','tr','us'])
print("\nEncode edilmiş ülkeler, DATAFRAME olarak:\n")
print(sonuc)

# yas diye adlandırmısız ama aslında sayısal veriler.
sonuc2=pd.DataFrame(data=boy_kilo_yas, index=range(22), columns=['boy','kilo','yas'])
print("\nEncode edilmiş boy kilo ve yaş, DATAFRAME olarak:\n")
print(sonuc2)

sonuc3=pd.DataFrame(data=cinsiyet_ft, index=range(22), columns=['cinsiyet']) # dummy varible dikkat!
print("\ncinsiyet, DATAFRAME olarak:\n")
print(sonuc3)

""" birleştirmelerin başladığı yer"""

s=pd.concat([sonuc,sonuc2],axis=1)
print("\nEncode edilmiş ülkeler ve boy-kilo-yaş, DATAFRAME olarak:\n")
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print("\nEncode edilmiş ülkeler, boy-kilo-yaş ve cinsiyet, DATAFRAME olarak:\n")
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
print('\n Boylar: \n')
print(boy)

sol=s2.iloc[:,:3]
sag=s2.iloc[:,4:]

veri=pd.concat([sol,sag], axis=1)

x_train, x_test, y_train, y_test=train_test_split(veri,boy,test_size=0.33, random_state=0) # verinin test/train yapısında bölünmesi

r2 = LinearRegression()
r2.fit(x_train, y_train)

y_pred=r2.predict(x_test) # tahmin
