# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    String=""
    if N==0 and N<0:
        return "-1"
    else:
        while N!=0:
            if N%2==0:
                String=String+"0"
            else:
                String=String+"1"
            N=int(N/2)
        return String
def laPalindrome(N):
    Tmp = N%10
    if N<0:
        return False
    while N!=0:
        DonVi=N%10
        N=int(N/10)
    KQ=DonVi
    if KQ==Tmp:
        return True
    else:
        return False
def laSoNguyenTo(K):
    if K < 2 :
        return False
    for i in range(2,K):
        if K %i==0:
            return False
    return True
def tongSoNguyenTo(N):
    KQ=0
    for i in range(1,N+1):
        if laSoNguyenTo(i):
            KQ=KQ+i
    return KQ
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()