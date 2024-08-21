# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:33:39 2024

@author: TuTrinh 
"""

#Cho chuỗi: Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM
import re 
address = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
#1. Tách thành các sub-string:
sub_strings = address.split(", ")

for sub_string in sub_strings:
    print(sub_string)


#2. Tách thành các sub-string:
address_cleaned = re.sub(r'\bP\. |\bQ\. |\bTp\. ', '', address)
sub_strings = address_cleaned.split(", ")

for sub_string in sub_strings:
    print(sub_string)