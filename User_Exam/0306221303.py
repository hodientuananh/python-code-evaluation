# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N>0:
       return bin(N)[2:]
    else:
        return "-1"        
    
def laPalindrome(N):
    if N>0:
        x=str(N)
        if x==x[::-1]:
            return True
        else:
            return False
    else:
        return False
    pass
def laSoNguyenTo(K):
    if K<2:
        return False
    elif K%1==0 and K%K==0:
        return True
    pass
def tongSoNguyenTo(N):
    tong=0
    if N<2:
        return 0
    for i in range (2,N+1):
            if laSoNguyenTo(i):
                tong+=i
    return tong
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main()