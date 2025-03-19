![image](https://github.com/user-attachments/assets/ed7bf03d-0a8b-46ba-8d74-3c9623b8a600)

Code giải:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


void printArray(vector <int> &v){
    int n=v.size();
    for (int i=0;i<n;i++){
        cout << v[i] << " ";
    }
    cout <<"\n";
}

void bubbleSort(vector <int> &v){
    int n = v.size();
    for (int i=0;i<n-1;i++){
        bool s=false;
        for (int j=0;j<n-1-i;j++){
            if (v[j]>v[j+1]){
                swap(v[j],v[j+1]);
                s=true;
                printArray(v);
            }
        }
        if (!s) break;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    vector <int> a(n);
    for (int i = 0 ; i<n ; i++){
        cin >> a[i];
    }
    bubbleSort(a);
    return 0;
}
```
