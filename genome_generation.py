# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:53:49 2022

@author: richi
"""

''' Escribir un programa que genere el genoma de una proteína ficticia
utilizando la matriz de transición de la Cadena 2 de una de las 4 proteínas'''
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
def virus(texto):
    f=open(texto)
    virus=f.read()
    f.close()
    virus=virus.replace("\n","")
    return virus

virusA=virus("A.txt")


bases=['G','T','A','C']
def matconfc2(virus):
    bd={}
    k=0
    prob=np.zeros((len(bases)**2,len(bases)))

    for i in range(len(virus)-2):
        bd[virus[i], virus[i+1]] = []

    for i in range(len(virus)-2):
        bd[virus[i], virus[i+1]].append(virus[i+2])

        
    for i in range(len(bases)**2):
        for j in range(len(bases)):
            
            prob[i,j]=bd[bases[k],bases[j]].count(bases[j])/(len(bd[bases[k],bases[j]])) #revisar por que no da exacto, denominador?
           
        k+=1
        if k==4:
            k=0 
    
    return prob    
        
prob=matconfc2(virusA)
cadena=rnd.choices(bases,k=2)
while len(cadena)<len(virusA): 
    for i in range(len(bases)):
        
        for j in range(len(bases)):
        
            if (cadena[-2]+cadena[-1])==(bases[i]+bases[j]):
                cadena=cadena+rnd.choices(bases,weights=(prob[4*i+j,:]),k=1)
                
    
'''Comprobamos si es correcto dibujando el histograma y comprobando si tiene una
distribucion similar a la del virus A'''

nbases=np.zeros(len(bases))
for i,b in enumerate(bases):
        nbases[i]=cadena.count(b)
plt.bar(bases, nbases)
plt.ylabel("Frecuencia")
plt.title("Mutación Virus A")
plt.show()
