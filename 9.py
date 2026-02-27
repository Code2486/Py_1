#دریافت عدد و چاپ مقسوم علیه های آن 

n = int(input("Enter your number : "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
