# :دریافت عددی به عنوان نمره کاربر و مشخص کردن وضعیت دانش آموز به طوری که اگر نمره بین 
C = 14-16
B = 16-18
A = 18-20

score = float(input("Enter student's score: "))
if 14 <= score < 16:
    print("Grade: C")
elif 16 <= score < 18:
    print("Grade: B")
elif 18 <= score <= 20:
    print("Grade: A")
else:
    print("Score is undifined!")
