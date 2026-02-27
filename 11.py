#دریافت عدد و چاپ اعداد زوج کوچکتر از آن

n = int(input("Enter your number : "))
for i in range(n):
    if i % 2 == 0:
        print(i)
