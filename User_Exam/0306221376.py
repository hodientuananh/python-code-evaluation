# Khai báo thư viện 
import math
# Khai báo biến 

# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):     
    if N>0:
        return bin(N)[2:]
    else :
        return "-1"
def laPalindrome(N):   
    if N<0:
        return False
    else:
        return str(N)==str(N)[::-1]
def laSoNguyenTo(K): 
    if K<0:
        return False
    for i in range(2,int (K**0.5)+1):
        if K%1==0:
            return False
        else :
            return True

def tongSoNguyenTo(N):  
   tong=0  
   if N<2:
       return False
   for t in range (2,N):
      if (laSoNguyenTo,t):
          tong+=t
          return tong

# Hàm main def main(): 
def main():
    N = int(input("Nhap vao so N: ")) 
    K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main 
if __name__ == "__main__": 
    main() 

