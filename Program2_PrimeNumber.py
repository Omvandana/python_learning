# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:06:10 2023

@author: hp
"""

num=21
flag=0
for i in range(2,num):
    flag=0
    if((num%i==0)&(num!=2)):
        flag=1
        break
if(flag==1):print("Number is not prime")
else:print("Number is prime")     
