class SinhVien :
    def __init__(self,ID,name,sexual,year):
         self.ID = ID
         self.name = name
         self.sexual = sexual
         self.year = year
   
while True:
    print("\nChon chuc nang:")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien bang ID")
    print("3. Xoa sinh vien bang ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo diem trung binh")
    print("7. Sap xep sinh vien theo diem trung binh")
    print("8. Sap xep sinh vien theo diem trung binh")
    print("0. Thoat")

    lua_chon = input("Nhap lua chon (0-8): ")
    if lua_chon == "1":
        print ("1")
    elif lua_chon == "2":
        print("2")
    elif lua_chon == "3":
        print("3")
    elif lua_chon == "4":
        print("4")
    elif lua_chon == "5":
        print("5")
    elif lua_chon == "6":
        print("6")
    elif lua_chon == "7":
        print("7")
    elif lua_chon == "8":
        print("8")
    elif lua_chon == "0":
        print("Thoat chuong trinh.")
        break
    else :
        print("Lua chon ko hop le.")
    
