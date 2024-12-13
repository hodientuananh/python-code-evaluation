# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N > 0:
        return bin(N)[2:]
    else :
        return "-1"
def laPalindrome(N):
    str_N=str(N)
    return str_N == str_N[::-1]
def laSoNguyenTo(K):
   if K < 2:
      return False
   for i in range (2,int(K**0.5)+1):
      if K % i == 0:
        return False
      return True

def tongSoNguyenTo(N):
    if N < 2:
       return 0
    tong = 0 
    for number in range(2,N + 1):
       if (laSoNguyenTo(number)):
          tong += number
    return tong
       


    
# Hàm main
def main():
 N = int(input("Nhap vao so N: "))
 K = int(input("Nhap vao so K: "))
 print("xuat chuoi nhi phan N: ", xuatChuoiNhiPhan(N))
 print("N co phai la so laPalindrome khong: ",laPalindrome(N))
 print("K la so nguyen to : ",laSoNguyenTo(K))
 print("tong so nguyen to la: ",tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
 main()
