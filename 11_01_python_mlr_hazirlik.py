# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print("\n Veriler \n")
print(veriler)

boy_kilo_yas=veriler.iloc[:,1:4]
print("\nBoy Kilo Yaş\n")
print(boy_kilo_yas)

#encoder: Kategorik -> Numeric - Ülkeler için
ulke = veriler.iloc[:,0:1].values
print("\n Ülkeler \n")
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()
print("\n Encoded Ülkeler \n")
print(ulke)

#encoder: Kategorik -> Numeric - Cinsiyetler için
c = veriler.iloc[:,-1:].values
print("\nCinsiyet\n")
print(c)


c_ft = le.fit_transform(veriler.iloc[:,-1])
print("\n Fit Transform Cinsiyet  \n")
print(c)


c = ohe.fit_transform(c).toarray()
#Dummy variable için yazılmış. 
#Aynı anda hem E/K hem de encoded versiyonu olmamalı..
#Öyle şekilde atılmalı ki son kalan kolondan yeterli çıkarım yapılabilmeli.
print("\n Encoded Cinsiyet - DUMMY VARIABLE/KUKLA DEĞİŞKEN\n") # (Dummy variable / Kukla değişken konusu devam) Burada olduğu gibi.
print(c)

#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print("\n Ülkeler - Dataframe:\n")
print(sonuc)

sonuc2 = pd.DataFrame(data=boy_kilo_yas, index = range(22), columns = ['boy','kilo','yas'])
print("\n Boy Kilo Yaş - Dataframe:\n")
print(sonuc2)

sonuc3 = pd.DataFrame(data = c_ft, index = range(22), columns = ['cinsiyet'])
print("\n Cinsiyet - Dataframe:\n")
print(sonuc3)

#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print("\n Ülkeler ve Boy-Kilo-Yaş - Dataframe:\n")
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print("\n Ülkeler, Boy-Kilo-Yaş ve Cinsiyet - Dataframe:\n")
print(s2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)