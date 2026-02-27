#دریافت ایام هفته از کاربر به صورت متن و چندمین روز هفته بودن را مشخص کردن

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
user_day = input("Enter the day of the week: ")
user_day = user_day.capitalize()
if user_day in days:
    print(user_day, "is day number", days.index(user_day) + 1, "of the week.")
else:
    print("Invalid day name!")
