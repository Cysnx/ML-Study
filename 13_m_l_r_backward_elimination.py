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

x_train, x_test, y_train, y_test=train_test_split(s,s2,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
Y_train=sc.fit_transform(y_train)
Y_test=sc.fit_transform(y_test)

# consturcting the model!



import stadsmodels.api as sm

X=np.append(arr=np.ones((22,1)).astype(int), values=veri, axis=1)