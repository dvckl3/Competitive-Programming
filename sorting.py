# all kind of sorting algo

def interchange_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a


def quick_sort(a):
    
