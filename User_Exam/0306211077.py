# Khai báo thư viện 
 
# Khai báo biến 
 
# Định nghĩa hàm 
def xuatChuoiNhiPhan(N):
      pass  
def laPalindrome(N):
     pass
     
            
def laSoNguyenTo(K): 
     
    for x in range(2,K):
         if K%x==0:
              return False
         else:
              continue
    return True
       
def tongSoNguyenTo(N):
      if N<=2:
           return 0
      a=0
      for x in range(2,N+1):
           if laSoNguyenTo(x)==True:
                a+=x
           else:
                continue
           
      return a

       
           
# Hàm main 
def main(): 
    N = int(input("Nhap vao so N: ")) 
   # print(xuatChuoiNhiPhan(N))
    #print(laPalindrome(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
#Gọi hàm main 
if __name__ == "__main__": 
    main() 
