a = ["CNTT",2023,"python"]
print("1.Phan tu dau, cuoi, giua")
print(f"phan tu dau: {a[0]}")
print(f"phan tu cuoi: {a[-1]}")
print(f"phan tu giua: {a[len(a)//2]}\n")

print("2.slice tu begin den end")
begin = int(input("begin:"))
end = int(input("end:"))
slice_a = a[begin:end]
print(f"List sau khi cat {slice_a}")

# add 
print("3.Them, xoa sua")
add = int(input("nhap vi tri can them:"))
add_index = int(input("nhap gia tri them:"))
a.insert(add,add_index)
print(f"List sau khi them {a}")

# remove
remove = int(input("nhap vi tri can xoa:"))
item = a.pop(remove)
print(f"Da xoa: {item}")
print(f"List con lai: {a}")

# update
update =  int(input("nhap vi tri can sua:"))
new = int(input("nhap gia tri moi:"))
a[update]= new 
print(f"List sau khi sua {a}")