# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(A):
    A=int(input("Nhap vao A: "))
    if not isinstance(A,int) or A<=0:
        return -1
    return bin(A)[2:]
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    x=int(input("Nhap vao so x: "))
    K=float(input("Nhap vao K bat ky: "))
    if K%x==1:
        print("True")
    else:
        print("false")
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    a=xuatChuoiNhiPhan(N)
    print(a)
    b=laSoNguyenTo(K)
    print (b)
# Gọi hàm main
if __name__ == "__main__":
    main()
