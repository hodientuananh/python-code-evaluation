# Khai báo thư viện
import math
# Khai báo biến

# Định nghĩa hàm
# def xuatChuoiNhiPhan(N):  
   
#   if N <= 0:
#     return "-1"  
#   nhiphan_string = ""
#   while N > 0:
#     nhiphan_string = str(N % 2) + nhiphan_string  
#     N //= 2
#   return nhiphan_string

# def laPalindrome(N):
#     if N <= 0:
#      return False
#     str_N = str(N)
#     nghichdao_N= int(str_N[::-1])
#     return N == nghichdao_N

def laSoNguyenTo(K):
    if(K<2):
     return False
    for i in range(2,K):
       if(K%i==0):
          return False
       return True
    
def tongSoNguyenTo(N):    
    tong = 0
    for N in range(2, N + 1):
     if laSoNguyenTo(N):
      tong=tong+N
    return tong
# pass
# # Hàm main
# def main():
N= int(input("Nhap vao so N: "))
# CÂU 3.1
# print(xuatChuoiNhiPhan(N)) 
# CÂU 3.2
# if laPalindrome(N):
#   print("True")
# else:
#   print("False")
# CÂU 3.3
print(laSoNguyenTo(N))
print('Tong so Nguyen to :')
print(tongSoNguyenTo(N))
# Gọi hàm main
#  if __name__ == "__main__":
#  main()