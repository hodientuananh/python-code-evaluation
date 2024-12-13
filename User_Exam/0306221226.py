# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):  
    if  N > 0:
        return bin (N) [2:]
    else:
        return "-1 "  

def laPalindrome(N): 
    if N > 0:
        str_n = str(N)
        return str_n == str_n[::-1]
    else:
        return False

def laSoNguyenTo(K): 
    if K < 2:
        return False
    for i in range(2, int(K ** 0.5)+1):
        if K % i == 0:
            return False
    return True
             

def tongSoNguyenTo(N):  
    if N < 2:
        return 0
    
    tong= 0

    for number in range(2, N + 1):
        if (laSoNguyenTo(number) == True):
           tong += number
           
    return tong

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
