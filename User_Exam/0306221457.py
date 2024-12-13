

# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if(N>1):
        xuatChuoiNhiPhan(N//2)
        return N%2
    pass
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if(K<2):
        return False
    else: 
        for i in range(2,K):
            if(K%i==0):
                return False
        return True
    

def tongSoNguyenTo(N):
    tong=0
    for i in range(2,N):
        if(laSoNguyenTo(i)):
            tong+=i
    return tong
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    #print('Chuoi nhi phan cua ',N,' la:',xuatChuoiNhiPhan(N))
    print('Tong so nguyen to: ',tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()