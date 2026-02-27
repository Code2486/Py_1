#دریافت عددی از ورودی و تشخیص آن که این عدد صفر هست یا منفی یا مثبت

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
