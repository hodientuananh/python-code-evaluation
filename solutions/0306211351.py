# Khai báo thư vien
# Khai báo biến 
# Định nghĩa hàm def 
 
def xuatChuoiNhiPhan(N):
      return "-1" if N <= 0 else (bin(N)[2:])
def laPalindrome(N):pass
    
    # return "true" if (N >= 0 ) & (N==N) else False
def laSoNguyenTo(K):   pass 
def tongSoNguyenTo(N):  pass
# Hàm main def main(): 
def main(): 
      N=int (input("nhap n:"))
      result_xuatchuoinhiphan=xuatChuoiNhiPhan(N)
      print(f"chuoi nhi phan:{xuatChuoiNhiPhan}")
    
# Gọi hàm main if __name__ == "__main__": 
if __name__ == "__main__": 
      main()
