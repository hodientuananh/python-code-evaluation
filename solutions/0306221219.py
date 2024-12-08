# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N > 0:
        return bin(N)[2:]
    else:
        return "-1"
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if ( K < 2 ):
        return False
    for i in range(2,int(K**0.5 + 1)):
        if(K%i==0):
            return False
    return True
        
def tongSoNguyenTo(N):
    sum = 0
    if (N<2):
        return 0
    for i in range(2,N-1):
        if(laSoNguyenTo(i)):
            sum+=i
    return sum
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))

    K = int(input("Nhap vao so K: "))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()