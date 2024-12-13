# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):    
     return bin(N)[2:] if N > 0 else "-1"
def laPalindrome(N):    
     if N < 0:
          return "False"
     else:
          laPalindrome = 0
     while N < 0 : 
          chusocuoi = N % 10
          laPalindrome = laPalindrome * 10 + chusocuoi
          N = N // 10 
     return"True"

     
def laSoNguyenTo(K): 
     return "True" if K % 2 != 0 else "False"       
def tongSoNguyenTo(N):    
     pass  
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: ")) 
    print(xuatChuoiNhiPhan(N))
    N = int(input("Nhap vao so N: ")) 
    print(laPalindrome(N))
    K = int (input("Nhap vao so nguyen to K:"))
    print(laSoNguyenTo(K))


# Gọi hàm main 
if __name__ == "__main__": main() 

