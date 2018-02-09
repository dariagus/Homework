import datetime 
def get_days_to_new_year():
    current_date = datetime.datetime.today()
    year = current_date.year + 1
    new_year = datetime.datetime(year, 1, 1)
    days_left = new_year - current_date

    return days_left.days

print(get_days_to_new_year())
