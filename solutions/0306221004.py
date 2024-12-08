# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):    
 pass
"""def laPalindrome(N):     
  N=0
  if(N>=0):
    return True
  else:
    (N<0)
    return False"""
def laSoNguyenTo(K):
    i=2
    while i<=K/2:
        if K%i==0:
            return False
        i+=1
    return True     
K=int(input("Nhap so nguyen to: "))
if K>1:
    print(f"So {K} la so nguyen to!")
else:
    print(f"So {K} khong la so nguyen to")
def tongSoNguyenTo(N):     
    tong=0
    while N>0:
        tong=tong+N%10
        N=int(N/10)
    return tong 
# Hàm main def main(): 
N = int(input("Nhap vao so N: "))
print(laSoNguyenTo(N))
print(tongSoNguyenTo(N))
#print(tongSoNguyenTo(N))
# Gọi hàm main 
if __name__ == "__main__": 
 main() 
