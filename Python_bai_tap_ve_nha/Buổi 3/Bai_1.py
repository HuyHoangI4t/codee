danh_sach_nv = [
    {"maNV": "001", "hoten": "Nguyen Van A", "luongCB": 500000, "loaiNV": "van_phong", "so_ngay_lam_viec": 20, "so_san_pham": 0},
    {"maNV": "002", "hoten": "Le Thi B", "luongCB": 400000, "loaiNV": "ban_hang", "so_ngay_lam_viec": 0, "so_san_pham": 50},
    {"maNV": "003", "hoten": "Nguyen Thi C", "luongCB": 600000, "loaiNV": "ban_hang", "so_ngay_lam_viec": 0, "so_san_pham": 60}
]

def tinh_luong(nhan_vien):
    if nhan_vien["loaiNV"] == "van_phong":
        return nhan_vien["luongCB"] + nhan_vien["so_ngay_lam_viec"] * 150000
    elif nhan_vien["loaiNV"] == "ban_hang":
        return nhan_vien["luongCB"] + nhan_vien["so_san_pham"] * 18000
    
def xuat_dsNV(danh_sach_nv):
    if not danh_sach_nv:
        print("Danh sach nhan vien trong.")
        return
    print("Danh sach nhan vien:")
    for nv in danh_sach_nv:
        luong_thang = tinh_luong(nv)
        print(f"Ma NV: {nv['maNV']} \nHo Ten: {nv['hoten']} \nLuongCB: {nv['luongCB']} \nLuong Thang: {luong_thang}")

def tim_NV(maNV, danh_sach_nv):
    for nv in danh_sach_nv:
        if nv["maNV"] == maNV:
            return nv
    return None

def NV_cao_nhat(danh_sach_nv):
    return max(danh_sach_nv, key=lambda nv: tinh_luong(nv)) if danh_sach_nv else None

def NV_banhang_thap(danh_sach_nv):
    ban_hang = [nv for nv in danh_sach_nv if nv["loaiNV"] == "ban_hang"]
    if not ban_hang:
        return None
    return min(ban_hang, key=lambda nv: tinh_luong(nv))

while True:
    print("\nChon chuc nang:")
    print("1. Xuat danh sach nhan vien")
    print("2. Tim nhan vien theo ma")
    print("3. Nhan vien co luong cao nhat")
    print("4. Nhan vien ban hang co luong thap nhat")
    print("5. Thoat")
    lua_chon = input("Nhap lua chon (1-5): ")
    
    if lua_chon == "1":
        xuat_dsNV(danh_sach_nv)
    elif lua_chon == "2":
        ma_nv_can_tim = input("Nhap ma nhan vien can tim: ")
        ket_qua = tim_NV(ma_nv_can_tim, danh_sach_nv)
        if ket_qua:
            print(f"Thong tin nhan vien:\n{ket_qua}")
        else:
            print("Khong tim thay nhan vien.")
    elif lua_chon == "3":
        nv_cao_nhat = NV_cao_nhat(danh_sach_nv)
        if nv_cao_nhat:
            print(f"Nhan vien co luong cao nhat:\n{nv_cao_nhat}")
        else:
            print("Danh sach nhan vien trong.")
    elif lua_chon == "4":
        nv_banhang_thap = NV_banhang_thap(danh_sach_nv)
        if nv_banhang_thap:
            print(f"Nhan vien ban hang co luong thap nhat:\n{nv_banhang_thap}")
        else:
            print("Khong co nhan vien ban hang.")
    elif lua_chon == "5":
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le, vui long thu lai.")
