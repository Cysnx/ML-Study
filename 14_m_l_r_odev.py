#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('odev_tenis.csv')

#test
print(veriler)
# Sayısal verilerin alınması
Sayısal = veriler.iloc[:,1:3].values
print(Sayısal)
# Tüm sayısal veriler çekildi.

# Kategorik verilerin alınması

play = veriler.iloc[:,4:5].values
print(play)


wind = veriler.iloc[:,3:4].values
wind=wind.astype(int) # Eğer dönüştürme yapmazsan datayı boolean kabul ediyor.
#sonraki kontrolümde ('verilerim' diye geçiyor) bir şeyi değiştirmediğini farkettim.
# Data bütünlüğü açısından yine de astype olarak belirttim.
print(wind)


outlook= veriler.iloc[:,0:1].values
print(outlook)

# Tüm kategorik veriler çekildi.

# Kategorik verilerin, sayısallaştırılması
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

le=LabelEncoder()
ohe= OneHotEncoder(sparse_output=False) # Şimdilik sadece gerekli diyelim.
#Sparse Matris ve Dense Matris kavramları var.

play[:,0]=le.fit_transform(play[:,0]) # no ve yes'ler 1 ve 0'lara çevirildi.
print(play)

wind[:,0]=le.fit_transform(wind[:,0]) # false ve true'lar 1 ve 0'lara çevirildi.
print(wind)

# outlook ise daha farklı dönüştürülmeli. Çünkü bir verinin diğerine üstünlüğü yok. 
# Ör: FR , US, TR. Benim verimde ise sunny, overcast ve rainy var. 
# 3 kolonlu bir matrisim olmalı.

outlook=ohe.fit_transform(outlook[:,0:1])
print(outlook)

#şimdi ise verileri birleştireceğim. play tahmin edilecek.
son_verilerim=np.concat([outlook,Sayısal,wind], axis=1)
print(son_verilerim)

#data frame dönüşümü
son_verilerim=pd.DataFrame(son_verilerim,columns=['o','r','s','temp','hum','wind'])
print(son_verilerim)

play=pd.DataFrame(play,columns=['play'])

print(play)

print(type(son_verilerim),type(play))


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(son_verilerim.iloc[:,0:6],
                                               play.iloc[:,0],
                                               test_size=0.33,
                                               random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

#backward elimination

import statsmodels.formula.api as sm

X=np.append(arr=np.ones((14,1)).astype(int), values=son_verilerim, axis=1) # katsayı ataması

X_l=son_verilerim.iloc[:,[0,1,2,3,4,5]].values

r_ols=sm.ols(endog=son_verilerim.iloc[:,-1:],exog=X_l)
r=r_ols.fit()
print(r.summary())