# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:19:18 2024

@author: TuTrinh 
"""

#1. Tách thành các sub-string
address = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = address.split(", ")

for sub_string in sub_strings:
    print(sub_string)

#2. Tách thành các sub-string

import re 
address = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
address_cleaned = re.sub(r"\bP\. |\bQ\. |\bTp\. ", "", address)
sub_strings = address_cleaned.split(", ")

for sub_string in sub_strings:
    print(sub_string)
    