# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):  
   
 if N <= 0:
   return "-1"  
 chuoinhiphan_string = ""
 while N > 0:
   chuoinhiphan_string = str(N % 2) + chuoinhiphan_string  
   N //= 2
 return chuoinhiphan_string 
def laPalindrome(N):
   if N <= 0:
     return False
   str_N = str(N)
   songhichdao_N= int(str_N[::-1])
   return N == songhichdao_N
def laSoNguyenTo(K):
    if(K<2):
      return False
    for i  in range(2,(K**0.5+1)):
        if (K%i==0):
            return False
        return True    
    pass
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print('Chuoi nhi phan:',xuatChuoiNhiPhan(N))
    N = int(input("Nhap vao so N: "))
    print('',laPalindrome(N))
# Gọi hàm main
if __name__ == "__main__":
    main()