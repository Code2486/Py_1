#دریافت عددی از ورودی و بیان اینکه چه روزی از هفته است(در صورتی که عددی نامعتبر وارد شود پیغام خطا نمایش داده شود)

day_num = int(input("Enter a number (1-7) for weekdays: "))
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if 1 <= day_num <= 7:
    print("Weekday:", days[day_num - 1])
else:
    print("Invalid number!")
