import math
N=0
def xuatChuoiNhiPhan(N):
    if N < 0:
        return "-1"
    else:
     return bin (N)[2:]
def laPalindrome(N):
 str_N =str(N)
 return str_N==str_N[::-1]
def laSoNguyenTo(K):
 if K<2:
  return False 
 for i in range (2,int (K**0.5)+1):
  if K % i==0:
      return False
 return True

def tongSoNguyenTo(N):
 tong=0
 for i in  range (2, N +1):
  if laSoNguyenTo(N):
    tong +=i
    return tong

def main():
 N = int(input("Nhap vao so N: "))
 K = int(input("Nhap vao so K: "))
 print(" Chuoi nhi phan cua N : ", xuatChuoiNhiPhan(N))
 print (" N co phai la so  Palindrome khong ? : ", laPalindrome(N))
 print ( "K co phai so nguyen to khong ? :  ", laSoNguyenTo(K))
 print ("Tong cac so nguyen to tu 2 den",N, "la",tongSoNguyenTo(N))

if __name__ == "__main__":
 main()