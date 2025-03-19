![image](https://github.com/user-attachments/assets/8b63126d-8606-43e8-a5de-baa8282b5088)

![image](https://github.com/user-attachments/assets/88d8f7c2-28c0-4349-8805-b9143f34b57e)

Code giải:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
void merge(vector <int> &a, int p, int q, int r){
    int n1=q-p+1;
    int n2=r-q;
    vector <int> L(n1),R(n2);
    for (int i =0; i < n1;i++){
        L[i]=a[p+i];
    }
    for (int j=0;j<n2;j++){
        R[j]=a[q+1+j];
    }
    int i = 0 ;
    int j = 0 ;
    int k = p;

    while (i<n1 && j < n2){
        if (L[i]<=R[j]){
            a[k]=L[i];
            i++;

        } else {
            a[k]=R[j];
            j++;
        }
        k++;
    }
    while (i<n1){
        a[k]=L[i];
        i++;
        k++;
    }
    while (j<n2){
        a[k]=R[j];
        j++;
        k++;
    }
    for (int x=0;x<p;x++){
        cout << a[x] << " ";
    }
    cout << "[ ";
    for (int x=p;x<=r;x++){
        cout <<a[x]<<" ";
    }
    cout << "] ";
    for (int x=r+1;x<a.size();x++){
        cout << a[x] << " ";
    }
    cout << "\n";

}
void MergeSort(vector <int> &a,int p, int r){
    if (p<r){
        int q=(p+r)/2;
        MergeSort(a,p,q);
        MergeSort(a,q+1,r);
        merge(a,p,q,r);
    }
}

int main(){
    int N;
    cin >> N;
    vector <int> a(N);
    for (int i=0;i<N;i++){
        cin >> a[i];
    }
    MergeSort(a,0,N-1);
    return 0;

}
```


