# Khai báo thư viện

# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    return  "-1"if N<0 else str(bin(N)[2:])
def laPalindrome(N):
    
    return "True" if (N>=0)&(N==N) else"False"
def laSoNguyenTo(K):
    K>=0
    return  "True"if (K>=2)&(K%2 !=0) else "False"
    
def tongSoNguyenTo(N):
    N>=2
    return str(sum(N)[2:N]) if N<2 else "0"
# Hàm main15
def main():
    N = int(input("Nhap vao so N: "))
    kq_xuatChuoiNhiPhan=xuatChuoiNhiPhan(N)
    print(kq_xuatChuoiNhiPhan)

    kq_laPalindrome=laPalindrome(N)
    print(kq_laPalindrome) 

    kq_TongSoNguyenTo=tongSoNguyenTo(N)
    print(kq_TongSoNguyenTo)

    K = int(input("Nhap vao so K: "))
    kq_laSoNguynTo=laSoNguyenTo(K)
    print(kq_laSoNguynTo)
# Gọi hàm main
if __name__ == "__main__":
    main()
