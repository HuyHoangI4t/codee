km = float(input("Nhap so km da di: "))
tien_cuoc = 0
if km <= 1:
    tien_cuoc = 15000
elif 1 < km <= 5:
    tien_cuoc = 15000 + (km - 1) * 13500
elif 5 < km <= 120:
    tien_cuoc = 15000 + 4 * 13500 + (km - 5) * 11000
else:  
    tien_cuoc = 15000 + 4 * 13500 + (120 - 5) * 11000
    tien_cuoc *= 0.9  
print(f"Số tiền cần trả: {tien_cuoc} VND")
