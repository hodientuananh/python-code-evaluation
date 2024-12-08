# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N): 
     if(N>=0):
          return bin(N)[2:]
     else:
         return -1
    

def laPalindrome(N):
  pass

def laSoNguyenTo(K):
    dem =2
    if(K<2):
        return False
    for i in range(2,K):
        if( K % i==0):
            dem=dem+1    
    if(dem == 2):
        return True
    else:
        return False

def tongSoNguyenTo(N):
    tong = 0
    for i in range (2,N+1):
        if(laSoNguyenTo(i)==True):   
            tong=tong+i
    return tong

# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
    print(laPalindrome(N))

# Gọi hàm main
if __name__ == "__main__":
    main()