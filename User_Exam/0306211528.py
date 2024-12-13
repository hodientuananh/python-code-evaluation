# Khai báo thư viện
import math
# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N <0: return "-1"
    tr =""
 
    while N>0:
 
        tr =N%2 + tr
        N=N/2
    return tr
def laPalindrome(N):
    if N/10%10==N%10: return "True"
    return"fales"

def laSoNguyenTo(K):
    while K<2:return 0
    a=2
    for i in range(2,a+1):
        if K%a==0:
            return "T"
    return"F"

    
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    kq =input(laPalindrome(N))


# Gọi hàm main
if __name__ == "__main__":
    main()