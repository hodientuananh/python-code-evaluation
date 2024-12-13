# Khai báo thư viện
import math 
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
#    if N<0:
#        return -1
#    else:
    pass
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    for x in range(2,K):
        if K%x==0:
            return False
        else:
             continue
    return True

def tongSoNguyenTo(N):
    if N<=2:
        return 0
    tong=0
    for x in range (2,N+1):
        if laSoNguyenTo(N)==True:
            tong=tong+x
        else:
            continue
    return tong
    
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()