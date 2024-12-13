# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
  if N <= 0:
    return "-1"  
  chuoinhiphan = ""
  while N > 0:
    chuoinhiphan = str(N % 2) + chuoinhiphan
    N //= 2
    return chuoinhiphan
    pass
def laPalindrome(N):
    if N <= 0:
     return False
    str_N = str(N)
    N_nghichdao= int(str_N[-1])
    return N == N_nghichdao
    pass

    
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print('xuatchuoinhiphan',N,'la:', xuatChuoiNhiPhan(N))
    # print('Tong so nguyen to la:',tongSoNguyenTo(N))
    print('nghichdao',N,laPalindrome(N))
# Gọi hàm main
if __name__ == "__main__":
    main()