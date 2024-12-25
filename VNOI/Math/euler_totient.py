# thuật chay tính phi hàm euler :)
def sieve(limit):
    A=[True for _ in range(limit+1)]
    A[0]=A[1]=False
    p=2 
    while (p*p<=limit):
        if A[p]==True:
            for j in range(p*p,limit+1,p):
                A[j]=False
        p+=1
    prime=[]
    for p in range (2,limit+1):
        if A[p]==True: 
            prime.append(p)
    return prime
def prime_fac_sieve(n):
    factors={}
    prime=sieve(n//2)
    for p in prime: 
        if p * p >= n:
            break
        while n % p == 0:
            if p in factors:
                factors[p] +=1
            else:
                factors[p]=1
            n//=p
    if n > 1 :
        factors[n]=1
    return factors



def euler_totient(n):
    prime_factors=prime_fac_sieve(n)
    result=1
    for p,exp in prime_factors.items():
        result *= (p**(exp)-p**(exp-1))
    return result
 
def main():
    import sys
    input = sys.stdin.read
    data=input().split()
    T=int(data[0])
    queries=list(map(int,data[1:]))

    result=[str(euler_totient(n)) for n in queries]
    sys.stdout.write("\n".join(result) + "\n")

if __name__== "main":
    main()

        
def compute_totient(limit):
    phi=list(range(limit+1))
    for p in range(2,limit+1):
        if phi[p] == p:
            for k in range(p,limit+1,p):
                phi[k]*=(p-1)
                phi[k]//=p
    return phi

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    queries = list(map(int, data[1:]))
    
    limit = max(queries)  
    phi = compute_totients(limit)
    
    results = [str(phi[n]) for n in queries]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()

def even_faster_phi(n):
    res=n
    i=2
    while i * i <= n: # vì các ước nguyên tố 
        #của n nếu có ước lớn nhất thì cũng không thể vượt quá n / 2 trừ khi n chính là một số nguyên tố. 
        if n % i == 0 :
            while n % i == 0:
                n//=i
            res-=res//i
        i += 1 
    if n > 1:
        res-=res//n # xử lí trường hợp n là số nguyên tố, hoặc n có ước nguyên tố lớn hơn căn n 
    return res
print(even_faster_phi(36))
