# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N == 0 :
        return '0'
    elif N < 0 :
        return N 
    ket_qua = ''
    while N > 0 :
        ket_qua = str(N % 2) + ket_qua
        N//=2
    return ket_qua
def laPalindrome(N):
    num=N
    new=0
    while N!=0 :
        a =N %10
        new = new *10+a
        N = N //10
    if new == num :
        return True
    else :
        return False
def laSoNguyenTo(K):
    if K <= 1 :
        return False
    for i in range (2,int(K**0.5)+1):
        if K % i == 0 :
            return False
    return True
def tongSoNguyenTo(N):
    sum = 0 
    for i in range (1,N) :
        if laSoNguyenTo(i) :
            sum += i
    return sum
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(f"Chuoi nhi phan cua {N}:{xuatChuoiNhiPhan(N)}")
    print(f"Ket Qua Doi Xung {N} :{laPalindrome(N)}")
    print(f"Ket qua kiem tra so nguyen to {N} :{laSoNguyenTo(N)}")
    print(f"Tong cac so nguyen to be hon so nguyen duong {N}:{tongSoNguyenTo(N)}")
# Gọi hàm main
if __name__ == "__main__":
    main()
    