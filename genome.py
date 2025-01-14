# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:12:29 2022

@author: richi
"""
import numpy as np
import matplotlib.pyplot as plt


def virus(texto):
    f=open(texto)
    virus=f.read()
    f.close()
    virus=virus.replace("\n","")
    return virus

virusA=virus("A.txt")
virusB=virus("B.txt")
virusC=virus("C.txt")
virusD=virus("D.txt")

bases=['G','T','A','C']

def nbases(virus,nombre):
    bases=['G','T','A','C']
    nbases=np.zeros(len(bases))
    for i,b in enumerate(bases):
        nbases[i]=virus.count(b)
    plt.bar(bases,nbases)
    plt.ylabel("Frecuencia")
    plt.title(nombre)
    plt.show()
    
nbasesA=nbases(virusA,"Virus A")
nbasesB=nbases(virusB,"Virus B")
nbasesC=nbases(virusC,"Virus C")
nbasesD=nbases(virusD,"Virus D")
    


''' Cálculo matrices de transición Cadena 1'''

def matconfc1(virus):
    bd={}
    prob=np.zeros((4,4))
    for i in range(len(virus)-1): 
        bd[virus[i]]=[] 
        
    for i in range(len(virus)-1): 
        bd[virus[i]].append(virus[i+1])
        
    for i in range(len(bases)):
        for j in range(len(bases)):
            prob[i,j]=bd[bases[i]].count(bases[j])/len(bd[bases[i]])
       
    return prob
 
#Virus A 
Aprob=matconfc1(virusA)

#Virus B  
Bprob=matconfc1(virusB)

#Virus C 
Cprob=matconfc1(virusC)

#Virus D 
Dprob=matconfc1(virusD)


'''Ya tenemos las matrices de transición de la cadena 1 para todos los virus teniendo en cuenta
 que cada fila representa la pribabilidad de ir desde esa letra hasta la de la columna'''
 
''' Cálculo matrices de transición Cadena 2'''

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
#Virus A
Aprobc2=matconfc2(virusA)

#Virus B
Bprobc2=matconfc2(virusB)

#Virus C
Cprobc2=matconfc2(virusC)

#Virus D
Dprobc2=matconfc2(virusD)

 
