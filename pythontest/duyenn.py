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
    
    lua_chon = input("Nhap lua chon (1-5): ")
