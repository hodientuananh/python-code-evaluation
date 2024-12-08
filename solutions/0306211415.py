#Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    pass

def laPalindrome(N):
     pass
def laSoNguyenTo(K):
    if K<2:
        return False
    elif K>=2:
        for i in range(2,K,1):
            if K%i==0:
                return False    
        return True
def tongSoNguyenTo(N):
    tong=0
    if N<2:
        return 0
    elif N>=2:
        for i in range(2,N,1):
            if laSoNguyenTo(i):
                tong=tong+1
        return tong    
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
if __name__ == "__main__":
    main()