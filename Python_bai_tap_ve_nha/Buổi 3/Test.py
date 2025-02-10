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
    print("Danh sách nhân viên:")
    for nv in danh_sach_nv:
        luong_thang = tinh_luong(nv)
        print(f"Ma NV: {nv['maNV']}, Ho Ten: {nv['hoten']}, LuongCB: {nv['luongCB']}, Luong Thang: {luong_thang}")

def tim_NV(maNV, danh_sach_nv):
    for nv in danh_sach_nv:
        if nv["maNV"] == maNV:
            #print(f"Ma NV: {nv['maNV']}, Ho Ten: {nv['hoten']}, LuongCB: {nv['luongCB']}")
            return nv
    return "khong co NV"
    

def NV_cao_nhat(danh_sach_nv):
    return max(danh_sach_nv, key=lambda nv: tinh_luong(nv))

def NV_banhang_thap(danh_sach_nv):
    ban_hang = [nv for nv in danh_sach_nv if nv["loaiNV"] == "ban_hang"]
    if not ban_hang:
        return None
    return min(ban_hang, key=lambda nv: tinh_luong(nv))

xuat_dsNV(danh_sach_nv)
# ma_nv_can_tim = input("Nhap ma nv: ")
ma_nv_can_tim = "001"
print(f"Nhan vien can tim: \n{tim_NV(ma_nv_can_tim, danh_sach_nv)}")
print(f"Nhân viên có lương cao nhất:\n{NV_cao_nhat(danh_sach_nv)}")
print(f"Nhân viên bán hàng có lương thấp nhất:\n{NV_banhang_thap(danh_sach_nv)}")