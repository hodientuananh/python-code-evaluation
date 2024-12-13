# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm

def xuatChuoiNhiPhan(N):
    if N < 0:
        print(f"{-1}")
    elif N > 0:
        return (bin(N)[2:])
 
# def laPalindrome(N):


def laSoNguyenTo(K):
    if K <=1:
        return False
    elif K % 1 == 0 and K % K == 0:
        return True
   
def tongSoNguyenTo(N):
    dem = 0
    if N < 2 == 0:
        return 0
    for i in range (2, N+1):
        if laSoNguyenTo(i) == True:
            dem +=i
    return dem    


       
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N)) 
    print(laSoNguyenTo(N))




# Gọi hàm main
if __name__ == "__main__":
    main()