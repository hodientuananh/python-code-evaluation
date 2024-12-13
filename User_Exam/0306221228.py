# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):
    if N > 0:
        return bin(N)[2:]
    else: 
        return "-1"
    pass

def laPalindrome(N):
    if N > 0:
        string_N = str(N)
        return string_N == string_N[::-1]
    else:
        return False
    pass  

def laSoNguyenTo(K):
    i = 2
    count = 0
    if K >= 2:
        while (i <= K):
            if (K % i == 0):
                count+=1
            i+=1
        if count >= 2:
            return False
        else:
            return True
    else:
        return False
    pass      

def tongSoNguyenTo(N):
    i = 2
    tong = 0
    if N < 2:
        return 0
    while (i <= N):
        if (laSoNguyenTo(i) == True):
            tong += i
        i += 1
    return tong
    pass  
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: "))
    print (xuatChuoiNhiPhan(N))
    print (laPalindrome(N))
    print (laSoNguyenTo(N))
    print (tongSoNguyenTo(N))
# Gọi hàm main 
if __name__ == "__main__": 
    main() 