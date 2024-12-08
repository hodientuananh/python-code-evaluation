# Khai báo thư viện

# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(a):
    if isinstance(a, int) and a >= 0:
        return bin(a)[2:]
    else:
        return "-1"

def laPalindrome(a):
    if isinstance(a, int) and a >= 0:
        return str(a) == str(a)[::-1]
    else:
        return False

def laSoNguyenTo(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True

def tongSoNguyenTo(tong):
    if tong < 2:
        return 0
    total = 0
    for i in range(2, tong + 1):
        if laSoNguyenTo(i):
            total += i
    return total

# Hàm main
def main():
    try:
        N = int(input("Nhap vao so N: "))
    except ValueError:
        print("-1")
        return
    
    print("Chuoi nhi phan cua N:", xuatChuoiNhiPhan(N))
    print("N la so Palindrome:", laPalindrome(N))
    print("Tong so nguyen to be hon hoac bang N:", tongSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main()
