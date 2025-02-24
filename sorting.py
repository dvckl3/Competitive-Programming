# all kind of sorting algo

def interchange_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a


def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[len(a)//2]
    left = [x for x in a if x<pivot]
    middle = [x for x in a if x==pivot]
    right = [x for x in a if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
    
def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
    
    
