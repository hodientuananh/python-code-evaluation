# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if (N < 0):
        return -1
    else :
        return bin(N)[2:]
#def laPalindrome(N):
  
def laSoNguyenTo(K):
    if(K < 2):
        return False
    for i in range(2,int(K /2)+1 ):
        if(K % i ==0):
            return False
    return True

def tongSoNguyenTo(N):
    sum = 0
    if(N < 2):
        return 0
    for num in range(2,N+1):
        if(laSoNguyenTo(num)):
            sum +=num
    return sum
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()