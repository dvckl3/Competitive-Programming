![image](https://github.com/user-attachments/assets/aea90ad7-5c26-467d-8270-9aed787d3631)
Code giải:
```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


void printArray(vector <int> &v){
    for (int i = 0 ; i<v.size() ; i++){
        cout << v[i] << " ";
    }    
    cout <<"\n";
}
void insertionSort(vector <int> &v){
    for (int i=1; i<v.size();++i){
        int key=v[i];
        int j = i-1;
        // đầu tiên ta tạo một key để lưu giá trị của v[i]
        // tiếp theo ta sẽ tạo một giá trị j=i-1 chính là ô trước đó
        // bước kế tiếp là so sánh xem thử v[j] so với v[i] như nào, nếu v[i]<=v[j] thì đổi vị trí i,j
        // nếu v[i]>v[j] thì giữ nguyên
        while (j>=0 && key<=v[j]){
            v[j+1]=v[j];
            j=j-1;
            printArray(v);
            
        }
        v[j+1]=key;
        printArray(v);
        
    }
}

int main(){
    int n;
    cin >> n;
    vector <int> a(n);
    for (int i = 0 ;i<n;i++){
        cin >> a[i] ;
    }
    insertionSort(a);
    return 0;

}
```
