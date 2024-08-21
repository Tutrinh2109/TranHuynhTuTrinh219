# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:21:40 2024

@author: TuTrinh 
"""
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

A = (((math.sqrt(a))-(math.sqrt(b))) / ((pow(a,0.25))-(pow(b,0.25)))) - (((math.sqrt(a))+(pow(a*b,0.25)))/((pow(a,0.25))+(pow(b,0.25))))
print("Kết quả: ",round(A))

