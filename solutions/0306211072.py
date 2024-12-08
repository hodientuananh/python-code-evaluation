# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if (N <=0):
        return "-1"
    ChuoiNhiPhan =""
    while N > 0:
        ChuoiNhiPhan =str(N % 2)+ChuoiNhiPhan
        N//=2
        return ChuoiNhiPhan
     

def laPalindrome(N):
    pass

def laSoNguyenTo(K):
    if(K<=2):
        return False
    if(K % K ==1 % K % 1 ==K):
        pass
    else:
        return False    

def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    ChuoiNhiPhan= xuatChuoiNhiPhan(N)
    print(ChuoiNhiPhan)
    K =int(input("Nhap so nguyen to K: "))
    SoNguyenTo = laSoNguyenTo(K)
    print(SoNguyenTo)

# Gọi hàm main
if __name__ == "__main__":

    main()
