# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:59:02 2024

@author: TuTrinh 
"""
 
#Viết chương trình cho phép nhập vào giờ, phút và giây

gio = int(input("Nhập vào giờ: "))
phut = int(input("Nhập vào phút: "))
giay = int(input("Nhập vào giây: "))
so_giay = (gio * 3600) + (phut * 60) + giay
print(f"Tổng số giây là: {so_giay} giây") 
