# Khai báo thư viện
import math
# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
pass
def laPalindrome(N):
pass
def laSoNguyenTo(K):
    if K>=0 or K==1: return "True"
    else:
        if K==2 : return "false"
        else:
            i = K-1
            while i>=1:
                if i==1:
                    return "True"
                if K % i==0 :
                    return "false"
                i-=1      

def tongSoNguyenTo(N):
    KQ = 0
    i = N
    while i > 0:
        if laSoNguyenTo(i) == "True":
            KQ += i
            i -= 1
    return KQ   

# Hàm main
def main():   
N = int(input("Nhap vao so N: "))

print (xuatChuoiNhiPhan(N))

# Gọi hàm main
if __name__ == "__main__":
main()