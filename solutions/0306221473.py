# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if (N<=0):
        return -1
    else:
        a=str(bin(N)[2:])
        return a
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if (K<2):
        return False
    for i in range(2,K):
            if(K%i==0):
                return False
    return True
def tongSoNguyenTo(N):
    tongsnt=0
    if(N<2):
        return 0
    for i in range (2,N+1):
        if(laSoNguyenTo(i)):
            tongsnt=tongsnt+i
    return tongsnt
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()