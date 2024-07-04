from datetime import datetime

def get_days_from_today(date : str):
   try:
     datetime_date = datetime.strptime(date, '%Y-%m-%d')
     delta = datetime_date - datetime.now()
     return delta.days
   except ValueError:
      return None

days_diff = get_days_from_today("2024-07-01")
if days_diff is None:
   print("Date has an incorrect format")
else:
   print(f"Difference in days from NOW is {days_diff}")