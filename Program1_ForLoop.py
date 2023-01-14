# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:53:40 2023
@author: Vandana

# write a program to find numbers divide by 3 , 5 and both and print the
numbers

"""

num = 30
for temp in range (1,num):
    if(temp%3==0):print(str(temp)+"is divisible by 3")
    if(temp%5==0):print(str(temp)+"is divisible by 5")
    if((temp%3==0)&(temp%5==0)):print(str(temp)+"is divisible by 3 & 5 Both")
