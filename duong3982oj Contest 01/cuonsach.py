# https://oj.duong3982.com/problem/contest01_b
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


def main():
    def count_digits(pages):
        digits = 0
        n=int(math.log10(pages)) + 1
        digits += n * (pages - 10**(n-1)+1)

        for i in range(1,n):
            digits += i*(9*10**(i-1))
        return digits

    def find_pages(digits): # dùng binary search để tìm số trang dựa vào x
        low,high=1,digits
        mid=(low+high)//2
        while low<=high:
            mid = (low+high)//2
            if digits == count_digits(mid):
                return mid
            elif digits > count_digits(mid):
                low = mid +1 
            else: 
                high = mid - 1 
        return -1
    q=inp()
    result = []
    for _ in range(q):
        t,x=mul()
        if t==1:
            result.append(count_digits(x))
        elif t==2:
            result.append(find_pages(x))

    stdpr("\n".join(map(str,result)))
if __name__ == "__main__":
    main()
