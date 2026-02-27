#دریافت عدد در مبنای ده دهی و تبدیل آن به مبنای دودویی و برعکس

n = int(input("Decimal Number : "))
result = ""
while n > 0:
    result = str(n % 2) + result
    n //= 2
print(result)


a = input("Binary number: ")
print(int(a, 2))
