# khỏi tạo t tuple có mỗi phần tử là kiểu dữ liệu đã học(str , int , float, dict , list, tuple) truy cập đến và thay đổi nó 
tuple = (
    "hello",2025,23.23,{"hello": "wordl"},[1,2,3],(4,5,6)
)

print(f"tuple ban dau:\n{tuple}")
tuple[3]["hello"]= "python"
print(f"tuple sau khi sua dict:{tuple}")
tuple[4][2]=5
print(f"tuple sau khi sua list:{tuple}")