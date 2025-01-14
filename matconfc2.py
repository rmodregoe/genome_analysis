# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:46:11 2022

@author: richi
"""
import numpy as np
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
            
            prob[i,j]=bd[bases[k],bases[j]].count(bases[j])/len(bd[bases[k],bases[j]])
           
        k+=1
        if k==4:
            k=0 
    
    return prob 