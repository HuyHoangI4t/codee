# bai tap 1 chuong 3
import datetime as dt

class Person:
    def __init__(self, name, sex, year, phone):
        self.name = name
        self.sexual = sex
        self.year = year
        self.phone = phone 

    @staticmethod
    def age(yob):
        Year = dt.datetime.now().year
        return Year - yob

    def print_info(self):
        print(self.name +" " + str(Person.age(self.year)), "tuổi")
        print(self.name + " có số điện thoại là " + self.phone)

class SinhVien(Person):
    sv = 0
    sv_list = []

    def __init__(self, name, sex, year, phone, name_class, sv_id, toan, ly, hoa):
        super().__init__(name, sex, year, phone)
        self.name_class = name_class
        self.sv_id = sv_id
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.diem_tb = round((toan + ly + hoa) / 3, 2)
        self.hoc_luc = self.xep_loai()
        SinhVien.sv += 1
        SinhVien.sv_list.append(self)
    
    def xep_loai(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung Bình"
        else:
            return "Yếu"

    @classmethod
    def sv_count(cls):
        print(f"Số lượng sinh viên hiện tại là: {SinhVien.sv}")

    def print_info(self):
        super().print_info()
        print(f"Lớp: {self.name_class}, ID: {self.sv_id}, Điểm TB: {self.diem_tb}, Học lực: {self.hoc_luc}")

def them_sinh_vien():
    name = input("Nhập tên: ")
    sex = input("Nhập giới tính: ")
    year = int(input("Nhập năm sinh: "))
    phone = input("Nhập số điện thoại: ")
    name_class = input("Nhập tên lớp: ")
    sv_id = input("Nhập ID sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    SinhVien(name, sex, year, phone, name_class, sv_id, toan, ly, hoa)
    print("Đã thêm sinh viên thành công!")

def hien_thi_ds():
    for sv in SinhVien.sv_list:
        sv.print_info()

def xoa_sinh_vien():
    sv_id = input("Nhập ID sinh viên cần xóa: ")
    SinhVien.sv_list = [sv for sv in SinhVien.sv_list if sv.sv_id != sv_id]
    SinhVien.sv -= 1
    print("Đã xóa sinh viên thành công!")

def tim_sinh_vien():
    name = input("Nhập tên sinh viên cần tìm: ")
    for sv in SinhVien.sv_list:
        if name.lower() in sv.name.lower():
            sv.print_info()

def sap_xep_theo_diem_tb():
    SinhVien.sv_list.sort(key=lambda sv: sv.diem_tb, reverse=True)
    print("Danh sách sinh viên sau khi sắp xếp theo điểm trung bình:")
    for sv in SinhVien.sv_list:
        print(f"{sv.name} - ID: {sv.sv_id} - Điểm TB: {sv.diem_tb}")

def sap_xep_theo_ten():
    SinhVien.sv_list.sort(key=lambda sv: sv.name)
    print("Danh sách đã được sắp xếp theo tên.")

def sap_xep_theo_id():
    SinhVien.sv_list.sort(key=lambda sv: sv.sv_id)
    print("Danh sách đã được sắp xếp theo ID.")

def cap_nhat_sinh_vien():
    sv_id = input("Nhập ID sinh viên cần cập nhật: ")
    for sv in SinhVien.sv_list:
        if sv.sv_id == sv_id:
            sv.name = input("Nhập tên mới: ")
            sv.sexual = input("Nhập giới tính mới: ")
            sv.year = int(input("Nhập năm sinh mới: "))
            sv.phone = input("Nhập số điện thoại mới: ")
            sv.name_class = input("Nhập tên lớp mới: ")
            sv.toan = float(input("Nhập điểm Toán mới: "))
            sv.ly = float(input("Nhập điểm Lý mới: "))
            sv.hoa = float(input("Nhập điểm Hóa mới: "))
            sv.diem_tb = round((sv.toan + sv.ly + sv.hoa) / 3, 2)
            sv.hoc_luc = sv.xep_loai()
            print("Thông tin sinh viên đã được cập nhật.")
            return
    print("Không tìm thấy sinh viên với ID đã nhập.")

while True:
    print("\nChọn chức năng:")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên bằng ID")
    print("3. Xóa sinh viên bằng ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Sắp xếp sinh viên theo ID")
    print("8. Hiển thị danh sách sinh viên")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn (0-8): ")
    if lua_chon == "1":
        them_sinh_vien()
    elif lua_chon == "2":
        cap_nhat_sinh_vien()
    elif lua_chon == "3":
        xoa_sinh_vien()
    elif lua_chon == "4":
        tim_sinh_vien()
    elif lua_chon == "5":
        sap_xep_theo_diem_tb()
    elif lua_chon == "6":
        sap_xep_theo_ten()
    elif lua_chon == "7":
        sap_xep_theo_id()
    elif lua_chon == "8":
        hien_thi_ds()
    elif lua_chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
