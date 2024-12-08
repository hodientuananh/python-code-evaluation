# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    return "-1" if N <= 0 else (bin(N)[2:])
    pass
def laPalindrome(N):
    return "True" if (N >= 0) & (N == N) else "False"
    pass
def laSoNguyenTo(K):
    return "True" if(K >= 2) & (K % 2 != 0) else "False"
    pass
def tongSoNguyenTo(N):
    return sum[2:N] if N >= 2 else "0"
    pass
# Hàm main
def main():
 N = int(input("Nhap vao so N (bai 3.1): "))
 result_xuatChuoiNhiPhan=xuatChuoiNhiPhan(N)
 print(f"Xuat chuoi nhi phan: {result_xuatChuoiNhiPhan}")


 N = int(input("Nhap vao so N (bai 3.2): "))
 result_laPalindrome=laPalindrome(N)
 print(f"So nguyen duong do la: {result_laPalindrome}")


 K = int(input("Nhap vao so K (bai 3.3): "))
 result_laSoNguyenTo=laSoNguyenTo(K)
 print(f"So nguyen duong do la: {result_laSoNguyenTo}")

 N = int(input("Nhap vao so N (bai 3.3): "))
 result_tongSoNguyenTo=tongSoNguyenTo(N)
 print(f"Tong so nguyen to la: {result_tongSoNguyenTo}")
# Gọi hàm main
if __name__ == "__main__":
 main()