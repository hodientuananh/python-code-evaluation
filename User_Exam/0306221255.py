# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):     
    if not isinstance(N, int) or N <= 0:
        return "-1"
    return bin(N)[2:]
def laPalindrome(N):     
    if N > 0:
        daong = str(N)
        return daong == daong[::-1]
    else:
        return False
def laSoNguyenTo(K):  
    if K < 2:
        return False
    for i in range(2, int(K ** 1/2) + 1):
            if (K % i == 0):
                return False    
    return True

def tongSoNguyenTo(N):   
    if N < 2:
        return 0
    sum = 0
    for num in range(2, N + 1):
        if laSoNguyenTo(num):
            sum += num

    return sum
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: ")) 
    K = int(input("Nhap vao so K: ")) 
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
   
# Gọi hàm main
if __name__ == "__main__": 
    main() 
