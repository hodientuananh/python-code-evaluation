# Khai báo thư viện
import math
# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    i=2
    while i<N/2:
        if N%2 == 0:
            return False
        i=i+1
        return True
    

def laPalindrome(N):
    i=min
    while i<max:
        if xuatChuoiNhiPhan(i):
            print ({i})
            i=i+1


def laSoNguyenTo(K): 
    if K==0 and K==1:
        return "True"
    else:
        if K==2:return "False"
        else:
            i=K+1
            while i>=1:
                if i==1:
                    return "true"
                if K%i==0:
                    return "false"
                i-=1
    
def tongSoNguyenTo(N):
    kq=0
    i=N
    while i<=N and i>0:
        if laSoNguyenTo(i)=="True":
            Kq+=1
            i+=1
    return Kq           


        

    

# Hàm main

def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main
#if __name__ == "__main__":
#main()