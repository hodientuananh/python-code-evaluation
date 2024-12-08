# Khai báo thư viện
import math

# Khai báo hàm

# Hàm xuất chuỗi nhị phân của N
def xuatChuoiNhiPhan(N):
    return bin(N)[2:]

# Hàm kiểm tra N có phải là số Palindrome không
def laPalindrome(N):
    return str(N) == str(N)[::-1]

# Hàm kiểm tra K có phải là số nguyên tố không
def laSoNguyenTo(K):
    if K < 2:
        return False
    for i in range(2, int(math.sqrt(K)) + 1):
        if K % i == 0:
            return False
    return True

# Hàm tính tổng các số nguyên tố nhỏ hơn hoặc bằng N
def tongSoNguyenTo(N):
    return sum(K for K in range(2, N + 1) if laSoNguyenTo(K))

# Hàm main
def main():
    N = int(input("Nhập vào số N: "))
    
    # Xuất chuỗi nhị phân của N
    print(f"Chuỗi nhị phân của {N}: {xuatChuoiNhiPhan(N)}")
    
    # Kiểm tra số N có phải là số Palindrome
    if laPalindrome(N):
        print(f"{N} là số Palindrome.")
    else:
        print(f"{N} không phải là số Palindrome.")
    
    # Tính tổng các số nguyên tố nhỏ hơn hoặc bằng N
    print(f"Tổng các số nguyên tố nhỏ hơn hoặc bằng {N}: {tongSoNguyenTo(N)}")

# Gọi hàm main
if __name__ == "__main__":
    main()