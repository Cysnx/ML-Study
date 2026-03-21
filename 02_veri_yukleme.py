# libraries

import pandas as pd

veriler= pd.read_csv('veriler.csv')

print("Veriler:\n")
print(veriler)

boy=veriler[['boy']]
print("\nBoylar:\n")
print(boy)

boykilo=veriler[['boy','kilo']]
print("\nBoy ve Kilolar:\n")
print(boykilo)

class insan:
    boy=180
    def kosmak(self,b):# A METHOD defined in 'insan' class.
        return b+10
    # y= f(x)
    # f(x) = x+10

ali=insan() # Ali is defined as an object in 'insan' class.
print("\nCalling 'boy' as an attribute from ali object which was from 'insan' class.\n")
print(ali.boy) # An Attribute(Nitelik/Özellik) called from 'insan' class.
print("\nCalling 'kosmak' as a method from 'ali' object from 'insan' class.\n")
print(ali.kosmak(90)) # Calculation of a METHOD defined in 'insan' class.


# Note: Non-Used libraries are deleted.