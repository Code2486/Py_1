#دریافت عددی و چاپ اعداد زوج دو رقمی کوچکتر از آن

n = int(input("Enter your number : "))
for i in range(10, n):
    if i % 2 == 0 and i < 100:
        print(i)
