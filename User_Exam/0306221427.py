# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
   if N <= 0: return -1
   if N > 0:
       sonhiphan= bin(N)[2:]
       return str(sonhiphan)

def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    dem = 0
    if K < 1: return False
    for i in range(1 ,K+1 ):
        if K % i == 0:
            dem += 1
        else: continue
    if dem == 2:
        return True
    else: False

def tongSoNguyenTo(N):
    tong = 0
    for i in range(2 ,N ):
        if laSoNguyenTo(i):
            tong =tong + i
    return tong
    
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
    


# Gọi hàm main
if __name__ == "__main__":
    main()