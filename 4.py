#دریافت سه عدد و تشخیص بزرگ ترین و کوچک ترین آنها 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    max_num = a
if b > a:
    max_num = b
if c > b:
    max_num = c
    print("The number is:", max_num)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a < b:
    min_num = a
if b < a:
    min_num = b
if c < b:
    min_num = c
    print("The number is:", min_num)
