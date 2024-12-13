# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm



def phandu(so_bi_chia, so_chia):
 if so_chia == 0: 
  return "khong the chia cho 0" 
 return so_bi_chia % so_chia
def chuoi_nhi_phan(N):
 if N < 0:
  return "So phải là số nguyên không âm. "
 if N ==0:
  return "0"
 chuoi_nhi_phan =""
 while N > 0:
  phandu=N % 2
  chuoi_nhi_phan=str(phandu) + chuoi_nhi_phan
  N=N // 2
  return chuoi_nhi_phan
def xuatChuoiNhiPhan(N):
 if N < 0:
  return "N phai la so nguyen duong"
 chuoi_nhi_phan=bin(N)[2:]
 return chuoi_nhi_phan

def laSoNguyenTo(K):
    if K < 2:
        return False
    for i in range (2, int(K**0.5)+1):
        if K % i == 0:
          return False
        return True
    
 
    pass


    pass
def tongSoNguyenTo(N):
     tong =0
     for i in range(2, N + 1):
       if laSoNguyenTo(i):
         tong+=i
         return tong
# Hàm main  
def main():
     
         N = int(input("Nhap vao so N: "))
         print(xuatChuoiNhiPhan(N))

K = int(input("Nhap vao so K: "))
print(laSoNguyenTo(K))

N = int(input("Nhap vao so nguyen to N: "))
print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":  
  main()


   
