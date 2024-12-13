# Khai báo thư viện 
import math
# Khai báo biến 
 
# Định nghĩa hàm  
def xuatChuoiNhiPhan(N):
    i=2
    while i<N/2:
     if N%i == 0:
        return False
     i+=1
     return True
def laPalindrome(N): 
   
   pass

def laSoNguyenTo(K):
    K=int(input("nhap vao so nguyen k:"))
    if xuatChuoiNhiPhan(K):
        print(" la so nguyen so")
    else:
        print("la so nguyen so")
def tongSoNguyenTo(N):
    tong=0
    while N>0:
        tong =tong +N%10
        N=int(N/10)
    return tong
# Hàm main def main(): 
def main():
    N = int(input("Nhap vao so N: ")) 
    print(laSoNguyenTo(N))
    print(xuatChuoiNhiPhan(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__": 
 main() 
