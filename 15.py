#دریافت دو عدد و چاپ اعداد زوج یا فرد بین دو عدد با انتخاب کاربر

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
select = input("Select even or odd?")
for i in range(a, b + 1):
    if select == "even" and i % 2 == 0:
        print(i)
    elif select == "odd" and i % 2 != 0:
        print(i)
