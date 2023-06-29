""" Determinar la radiación espectral [W/(m2um)] como cuerpo negro de una 
estrella (T=20000 K) y compararla con la del Sol (T=5778 K) y la Tierra 
(T=287.65 K), desde 0.1 um a 100 um en intervalos de 0.05 um. Graficar los 
resultados obtenidos """
from math import *
import matplotlib . pyplot as plt
import pandas as pd
import numpy as np

""" x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

y = [5 , 2 ,4 , 4 , 8 , 7 , 4 , 8 , 10 , 9]

plt . plot (x , y)
plt . xlabel ( 'Time ( s ) ' )
plt . ylabel ( ' Temperature (degC) ' )
plt . show () """


Ts= 20000
h=6.626176*10**(-34)
c= 2.997923*10**(8)
k= 1.380662*10**(-23)

#T=Ts*sqrt(h)*exp(k)
#print(T)
valores_s=[]
valores_lam=[]
def radiacion_espectral(lam):
    

    s=(2*pi*h*c**2)/(lam**5*(exp((h*c)/(k*lam*Ts))-1))*10**(-6)
    
 
    return s

ini=0.1*10**(-6)
fin= 100*10**(-6)
increm=0.05*10**(-6) 
for i in np.arange(ini,fin,increm):
    #radiacion_espectral(i)
    a=radiacion_espectral(i)
    valores_s.append(a)
    valores_lam.append(i*10**6)


data = {'radiacion': valores_s, 'lambda': valores_lam}

df = pd.DataFrame(data, columns = ['radiacion', 'lambda'])

df.to_excel ('agregan la ruta donde quieren que se guarde', index = False, header=True)

print("hello")
