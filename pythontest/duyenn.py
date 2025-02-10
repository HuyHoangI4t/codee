list = [("Tiền Giang", 63), ("Long An", 62), ("Vĩnh Long", 64), ("Bình Dương", 60)]
new_list = sorted(list, key=lambda x: x[1])
print(f"List ban dau:         {list}")
print(f"List sau khi sap xep :{new_list}")
