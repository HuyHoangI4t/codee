a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a + b > c and a + c > b and b + c > a:
    print("Co the tao mot tam giac:")
    if a == b == c:
        print("Day la tam giac deu.")
    elif a == b or b == c or c == a:
        print("Day la tam giac can.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Day la tam giac vuong.")
    else:
        print("Day la tam giac thuong.")
else:
    print("Khong tao thanh tam giac.")