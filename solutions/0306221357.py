# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N==0:
        return '0'
    elif N<0:
        return N
    result=''
    while N>0:
        result=str(N%2)+result
        N//=2
    return result
def laPalindrome(N):
    num=N
    newNUm=0
    while N!=0:
        a=N%10
        newNUm=newNUm*10+a
        N=N//10
    if newNUm==num:
        return True
    else: 
        return False
def laSoNguyenTo(K):
    i=2
    if K <2 :
        return False
    elif K>=2:
       while i <K:
           if K%i==0:
               return False
           i=i+1
    return True
                 
def tongSoNguyenTo(N):
    tongSNT=0
    while N>0:
        if laSoNguyenTo(N)==True:
            tongSNT+=N
        N-=1
    return tongSNT
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print(laPalindrome(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()