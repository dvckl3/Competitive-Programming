import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

MOD=10*6

# Bài tập đại loại là cho một bảng a kích thước m*n và một số k 
# ta cần tìm một bảng con của bảng a, bắt đầu từ góc trên cùng bên trái là (u,v), góc dưới cùng bên phải là (p,q)
# sao cho tổng các phần tử trong bảng con đó không vượt quá k cho trước ở trên
# yêu cầu là tìm bảng con là bảng vuông có kích thước lớn nhất có thể có. 
# Bước đầu tiên là ta tính prefix sum 2 chiều của bảng a, sau đó tính tiếp các bảng con có thể có từ bảng a đó. 
# Thì công thức prefix sum cho mảng 2 chiều sẽ là prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+a[i-1][j-1]
# Công thức cho bảng ô vuông con từ (u,v) đến (p,q) là prefix[p][q]-prefix[u-1][q]-prefix[p][v-1]+prefix[u-1][v-1]
# bây giờ cách để tối ưu bài này ta tìm duyệt các bảng ô vuông thôi bằng tìm kiếm nhị phân.

def main():
    
    m,n,k=mul()
    a=[seq() for _ in range(m)]
    prefix=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+a[i-1][j-1]

    def getsum(u,v,p,q):
        return (prefix[p][q]-prefix[u-1][q]-prefix[p][v-1]+prefix[u-1][v-1])

    max_size=0
    left,right=1,min(m,n)
    while left<=right:
        size=(left+right)//2
        found=False

        for i in range(1,m-size+2):
            for j in range(1,n-size+2):
                if getsum(i,j,i+size-1,j+size-1) <=k:
                    found=True
                    break
            if found:
                    break
        if found: 
            max_size=size
            left=size+1
        else:
            right=size-1
    
    stdpr(max_size)
if __name__ == "__main__":
    main()
