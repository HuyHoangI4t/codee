print("Nhập 2 số a và b:")
a = int(input()) ; b = int(input())
x = ( (a+b) / ( a** (1/3) + b** (1/3)) - (a*b)**(1/3)) / ((a** (1/3) - b** (1/3))** 2)
print (round(x,1))