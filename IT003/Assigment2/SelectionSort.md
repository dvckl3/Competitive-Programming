
![image](https://github.com/user-attachments/assets/37283a48-acf6-43bf-a2bd-19527b2a49bb)

Code giải:
```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void printArray(vector <int> &v){
    for (int i = 0 ; i<v.size();i++){
        cout << v[i] << " ";
    }
    cout << "\n";
}

void selectionSort(vector <int> &v){
    int n=v.size();
    for (int i = 0 ; i<n-1;++i){
        int minId=i;
        for (int j =i+1;j<n; ++j){
            if (v[j]<v[minId]){
                minId=j;
            }
        }
        if (minId!=i){
            swap(v[i],v[minId]);
            printArray(v);
        }
        
    }


}
int main(){
    int n;
    cin >> n;
    vector <int> a(n);
    for (int i=0;i<n;i++){
        cin >> a[i];
    }
    selectionSort(a);


    return 0;

}
```
