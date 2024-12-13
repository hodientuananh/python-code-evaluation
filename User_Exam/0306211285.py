# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):     
    if not isinstance (N, int) or N<=0:
        return "-1"
    return bin (N)[2:]

def laPalindrome(N):     
    if not isinstance (N, int) or N<=0:
        return False
    str_N=str(N)
    return str_N==str_N[::-1]

def laSoNguyenTo(K): 
    if K < 2:
        return False
    for i in range(2, int(K**0.5)+1):
        if K % i==0:
            return False
    return True
def tongSoNguyenTo(N):     
    pass  
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: ")) 
# Gọi hàm main 
if __name__ == "__main__":
    main()
