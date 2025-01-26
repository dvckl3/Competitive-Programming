# code 1 :
def main():
    import sys
    input = sys.stdin.read  
    a, b = map(int, input().split()) 

    res = 1
    ok = False

    for i in range(1, b + 1):
        res *= a
        if res >= 1e6:
            ok = True
        res %= int(1e6) 
    if not ok:
        print(res)
    else:
        print(f"{res:06}")  

if __name__ == "__main__":
    main()

# code 2 : sau khi cài template cho nhìn sang 

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
    a,b=mul()
    res = 1 
    base = a 
    ok = True
    while b > 0 :
        if b % 2 == 1:
            res = (res*base) 
        base = (base*base)
        b//=2
    if res >= 1e6:
        res %= int(1e6)
    stdpr(res)


if __name__ == "__main__":
    main()
