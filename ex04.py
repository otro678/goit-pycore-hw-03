from datetime import datetime, timedelta

def get_upcoming_birthdays(users, shift_weekend_birthday_to_monday=True):
    today = datetime.now().date()
    one_week_forward = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if today <= birthday_this_year <= one_week_forward:
            congratulation_date = birthday_this_year

            if shift_weekend_birthday_to_monday:
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)
            else:
                if congratulation_date.weekday() == 5:
                    congratulation_date -= timedelta(days=1)
                elif congratulation_date.weekday() == 6:
                    congratulation_date -= timedelta(days=2)

            upcoming_birthdays.append({
                "name": user["name"],
                "birthday": birthday_this_year.strftime("%Y.%m.%d"),
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.07.04"},
    {"name": "Mister X", "birthday": "1981.05.03"},
    {"name": "Miss Y", "birthday": "1983.07.05"},
    {"name": "Jane Smith", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань у найближчі 7 днів, якщо іменинників з ДН на вихідних привітаємо у п'ятницю:\n", get_upcoming_birthdays(users, False))
print("Список привітань у найближчі 7 днів, якщо іменинників з ДН на вихідних привітаємо у понеділок:\n", get_upcoming_birthdays(users))