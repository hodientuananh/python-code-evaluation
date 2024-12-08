# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N < 0:
        print ("-1")
    elif N > 0:
       nhiphan = (bin(N)[2:])
       return (f"'{nhiphan}'")

       
#def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if K <= 1:
        return False
    elif K % 1 == 0 and K % K ==0: 
        return True


# def tongSoNguyenTo(N):


# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N)) 
    #print (laPalindrome(N))
    print(laSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main() 
