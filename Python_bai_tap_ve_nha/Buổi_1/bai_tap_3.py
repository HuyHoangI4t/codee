a = int(input("Nhap a: ")) ; b = int(input("Nhap b: "))
x = ( (a+b) / ( a** (1/3) + b** (1/3)) - (a*b)**(1/3)) / ((a** (1/3) - b** (1/3))** 2)
print("Ket qua:",round(x,1))