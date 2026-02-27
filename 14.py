#دریافت دو عدد و چاپ مقسوم علیه مشترک آنها

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i)
