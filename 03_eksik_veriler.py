# libraries

import pandas as pd
import numpy as np

veriler= pd.read_csv('eksikveriler.csv') # 02'ye göre dosya ismi değiştirildi.


print(f'eksik veriler: \n {veriler}')

boy=veriler[['boy']]
print('\nboy: \n',boy)

boykilo=veriler[['boy','kilo']]
print('\nboykilo: \n ',boykilo)

class insan:
    boy=180
    def kosmak(self,b):
        return b+10
    # y= f(x)
    # f(x) = x+10

ali=insan() # Ali is defined as an object in 'insan' class.
print("\nCalling 'boy' as an attribute from ali object which was from 'insan' class.\n")
print(ali.boy) # An Attribute(Nitelik/Özellik) called from 'insan' class.
print("\nCalling 'kosmak' as a method from 'ali' object from 'insan' class.\n")
print(ali.kosmak(90)) # Calculation of a METHOD defined in 'insan' class.
#missing values / eksikveriler konusunun başlangıcı.

from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
yas=veriler.iloc[:,1:4].values
print("\nImpute oncesi:\n") # mevcut durumu görmek için.
print(yas) 
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])
print("\nImpute sonrası:\n") # sonraki durumu görmek için.
print(yas)

# Note: Non-Used libraries are deleted.
