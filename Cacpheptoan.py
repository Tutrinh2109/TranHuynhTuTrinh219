# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:33:51 2024

@author: TuTrinh
"""

"""
Tính tổng, hiệu, tích, thương, chia lấy dư, chia lấy nguyên của 2 số trên và in kết quả ra màn
hình. Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm 
"""
#Nhập a,b:
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
#Các phép toán:
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không thể chia cho "
chia_lay_du = a % b if b != 0 else "Không thể chia cho "
chia_lay_nguyen = a // b if b != 0 else "Không thể chia cho "
#Làm tròn:
thuong_lam_tron_2 = round(a / b, 2) if b != 0 else "Không thể chia cho 0"
thuong_lam_tron_3 = round(a / b, 3) if b != 0 else "Không thể chia cho 0"
# Xuất:
print("Tổng 2 số nguyên là: ",tong)
print("Hiệu 2 số nguyên là: ",hieu)
print("Tích 2 số nguyên là: ",tich)
print("Thương 2 số nguyên là: ",thuong)
print("Thương làm tròn 2 số sau dấu chấm là: ",thuong_lam_tron_2)
print("Thương làm tròn 3 số sau dấu chấm là: ",thuong_lam_tron_3)
print("Chia lấy dư 2 số nguyên là: ",chia_lay_du)
print("Chia lấy nguyên 2 số nguyên là: ",chia_lay_nguyen)




