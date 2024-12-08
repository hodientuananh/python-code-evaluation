# Khai báo thư viện

# Khai báo biến
#N=int
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
 #pass
    if   N<=0:
         return"-1"
    else:
         return bin(N)[2:]

def laPalindrome(N):
 pass
def laSoNguyenTo(K):
 pass

def tongSoNguyenTo(N):
 pass

# Hàm main
def main():
 N = int(input("Nhap vao so N: "))
 print("Chuoi nhi phan cua N:",xuatChuoiNhiPhan(N))
# Gọi hàm main
if __name__ == "__main__":
 main()