# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N>0:
        return bin(N)[2:]
    else:
        return "-1"
def laPalindrome(N):
    if N>0: 
        str_N=str(N)
        if str_N ==str_N[::-1]: return True
        else: return False
    else: return False
def laSoNguyenTo(K):
    # if(K<=1):return False
    # if(K<=3):return True
    # for i in range (5,K):
    #     if(K%i==0 or K%(i+2)==0):
    #         return False
    # return True
    if K < 2:
        return False
    # elif K %1==0 and K%K==0: return True
    for i in  range (2,K):
        if K%i==0:
            return False
    return True
def tongSoNguyenTo(N):
    sum=0
    if N <2: return 0
    for i in range (2,N+1):
        if laSoNguyenTo(i)==True: 
            sum=sum+i
    return sum
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(N))
    print (tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()
