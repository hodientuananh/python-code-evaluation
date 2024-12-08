# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm

def xuatChuoiNhiPhan(N):

    if  N > 0:
        return  bin(N)[2:]
    else:
        return -1
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    pass
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))

    ketqua = xuatChuoiNhiPhan(N)
    if ketqua == -1:
        print("N khong phai la so nguyen duong")
    else:
        print("Xuat chuoi nhi phan" , ketqua)
# Gọi hàm main
if __name__ == "__main__":
    main()