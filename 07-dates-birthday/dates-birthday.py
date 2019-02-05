from datetime import date

def age_to_time(age):
    months = age * 12
    days = age * 360 
    hours = 24 * 360 * age
    minutes = 60 * 24 * 360 * age

    print(f'months : {months} \ndays : {days} \nhours : {hours}  \nminutes : {minutes}')


def birthday_to_time(mm_dd_yyyy):
      month_parse = int(mm_dd_yyyy[0:2])
      day_parse = int(mm_dd_yyyy[3:5])
      year_parse = int(mm_dd_yyyy[6:])
      borndate = date(year_parse, month_parse, day_parse)
      todays_date = date.today()
      
      days_alive = (todays_date - borndate).days
      months = days_alive // 30
      hours = days_alive * 24
      minutes = days_alive * 24 * 60

      print(f'months : {months} \ndays : {days_alive} \nhours : {hours} \nminutes: {minutes}')


print(age_to_time(1))


print(birthday_to_time("02-04-2018"))
"""
returns....
days :365
hours : 8760
minutes: 525600
Nonemonths : 12, days : 365, hours : 8760, minutes: 525600
"""


