from datetime import datetime
def get_days_from_today(date : str):
   datetime_date = datetime.strptime(date, '%Y-%m-%d')
   delta = datetime_date - datetime.now()
   return delta.days

days_diff = get_days_from_today("2024-07-01")
print(f"Difference in days from NOW is {days_diff}")