# CP in Python
Note lại một số lưu ý khi viết các thuật CP bằng ngôn ngữ Python. 

# Lý thuyết căn bản 

## 1. Kiểu dữ liệu trong Python
Trong python có 4 kiểu dữ liệu chính: Booleans, integers, floating-point numbers và character strings

- Booleans là kiểu dữ liệu logic chỉ đúng `True` hoặc sai `False`
- Integers là kiểu dữ liệu dùng để biểu diễn các số nguyên
- Floating-point numbers là kiểu dữ liệu dùng để biểu diễn các số thực
- Còn strings là các xâu kí tự, thường được đặt trong dấu nháy đơn hoặc kép

Gán một object cho một kiểu dữ liệu thì ta dùng các hàm `bool,int,float,str`. Ví dụ 7.5 là float nhưng ta gõ `print(int(7.5))` thì output sẽ là 7.

## 2. Cấu trúc dữ liệu trong python

### List
`list` trong python hay còn gọi là mảng là một kiểu dữ liệu cho phép ta lưu trữ nhiều kiểu dữ liệu khác.

Để khởi tạo một `list` ta dùng syntax `list=[]` và chỉ số bắt đầu của mảng là chỉ số 0 chứ không phải 1. Ví dụ
```
list=[1,2,3]
print(list[0]) #1
```
Mảng có các toán tử thao tác như sau:
- Đầu tiên là `append()` để thêm các phần tử vào cuối danh sách
- Để truy vấn vào phần tử cuối cùng của mảng ta sẽ gõ `list[-1]` và tương tự phần tử cuối cùng thứ 2 là `list[-2]`
- `list[i:j]` lấy danh sách các phần tử trong danh sách bắt đầu từ `i` và kết thúc ở `j-1`, ví dụ `list[:j]` sẽ lấy từ 0 tới j-1
- `list[i:]` lấy các phần tử từ i trở đi, bắt đầu từ i
- `list[-3:]` lấy 3 phần tử cuối của danh sách
- `list[i:j:k]` lấy từ i tới j-1 với bước nhảy là k
- `list[::2]` lấy các phần tử có chỉ số chẵn
- `list[::-1]` lấy nghịch đảo của list ban đầu

![image](https://github.com/user-attachments/assets/ebd82b5d-1779-4d37-b66b-91b1d1d6f8d0)

...

### Tuple
`Tuple` giống như `list` nhưng ta không thể thay đổi giá trị các biến một khi đã khai báo

Khai báo bằng ngoặc tròn `()` như sau: `tuple=(1,2,3)`

### Set
`Set` là một tập hợp không có thứ tự và cũng không trùng lặp phần tử. Khai báo bằng dấu ngoặc nhọn: `set={1,2,3}`

### Dict
`Dict` hay còn gọi là từ điển. Trong dict bao gồm một khóa và một từ điển tương ứng với khóa đó, ta có thể coi như là một ánh xạ.
Khai báo như sau: 

```
dict={"a" : 1,"b" : 1,"c" : 1}
print(dict["a"])
```
Khai báo các vòng lặp trong mảng hoặc dict

![image](https://github.com/user-attachments/assets/74530f7b-30ca-44b5-81b1-0791c946ac77)

## 3. List comprehension

List comprehension là cú pháp giúp khai báo các kiểu cấu trúc dữ liệu được ngắn gọn

![image](https://github.com/user-attachments/assets/935b92e1-66ff-4062-8445-76f1ef8f5a5a)

Một số lưu ý về việc gọi hàm `range` trong python

![image](https://github.com/user-attachments/assets/150247a3-2b15-4c65-ba84-5939ffb0f3b0)



# Các loại cấu trúc dữ liệu nâng cao 

## Nodes
Nodes là một trong những dạng cấu trúc dữ liệu căn bản bao gồm hai thành phần chính đó chính là data của nodes hiện tại và con trỏ chỉ đến các nodes khác, có thể là nodes kế tiếp hoặc nodes trước đó.

![image](https://github.com/user-attachments/assets/a39091ba-49be-45da-bd65-26a0f171b373)

Có 2 dạng cấu trúc dữ liệu khác được xây dựng dựa trên nodes đó là tree và linked list.

Một orphaned nodes là những nodes mà không bị trỏ tới bởi các nodes khác hoặc chỉ có liên kết đến head node. 
## Linked list
Linked list là tập hợp các nodes được liên kết với nhau. Node sau chứa link đến node trước. Một node chứa data và liên kết đến node tiếp theo

# Các thuật toán từ cơ bản đến nâng cao


