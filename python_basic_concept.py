# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Python Basic Concept

"""

# for loop

my_string = "amit kumar"
for a in my_string:
    print(a,end="")
    
    
    
    
# Provide range in for loop

colors = ["red","green","prink" ,"a"] 
type(colors)
colors[1]   

for i in range(1,3):
    print(colors[i],end="")
    
# range from 0 to 3 with every second index increment    
for i in range(0,3,2):
    print(colors[i],end=" ")
    
for i<range(0,3,2):
    print(colors[i],end=" ")   
    
# PASS concept - null operation

for i in colors:
    pass
    print(i,end=" ")
    print("skip")
    
# enumerate concept    




#String  which comes in double "" or single 'qoutes'

# even space in " " is consider as string.


# slicing 

my_val = 'Hello world'

my_val[:4]  # takes from starting 0 to 3rd index

my_val[:]  # default takes all string 0 to last

my_val[3:4]  # print only 3rd index


# Concatination

my_first = "vandana"
my_sec = 'singh'

my_new = my_first+my_sec
print(my_new," ",my_first , my_sec)


# String is immutable 

my_first[0]
my_first[0]='t'  # TypeError will show as str object does not support item assignment. as it is immutable

del.my_first[0] # it will also not work


# String in build methods
my_first.upper()
my_first.isalpha()
my_first.isalnum() # it returns true as alpha and num anyone existence is fine.






























    
    