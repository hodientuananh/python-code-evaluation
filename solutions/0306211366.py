# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):     
    return "-1" if N <= 0 else (bin(N)[2:])
    pass
def laPalindrome(N):
    return "true" if (N >= 0) & (N == N) else "False"    
    pass  
def laSoNguyenTo(K): 
    return "true" if (K>=2) & (K % 2 != 0)  else "False"
    pass      
def tongSoNguyenTo(N):
    return sum[2:N] if N >= 2 else "0"  
    pass  
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: "))
    KQL_xuatChuoiNhiPhan = xuatChuoiNhiPhan(N)
    print(f"xuat ket qua chuoi nhi phan la: {KQL_xuatChuoiNhiPhan}")

    N = int(input("Nhap vao so N: ")) 
    KQL_laPalindrome = laPalindrome(N)
    print(f"Xuat ket qua lapalindrome la :{KQL_laPalindrome}")

    K = int(input("Nhap vao so K: "))
    KQL_laSoNguyenTo = laSoNguyenTo(K)
    print(f"So nguyen to la: {KQL_laSoNguyenTo}")

    N = int(input("Nhap vao so N: "))
    KQL_tongSoNguyenTo = tongSoNguyenTo(N)
    print(f"ket qua tong so nguyen to la: {KQL_tongSoNguyenTo}")
# Gọi hàm main 
if __name__ == "__main__": 
    main() 
