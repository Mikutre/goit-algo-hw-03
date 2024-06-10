

def get_days_from_today(date):
  
  from datetime import datetime

  current_date = datetime.now()

  try :
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    return current_date.toordinal() - date_obj.toordinal()
  
  except:
    print('Wrong format')

print(get_days_from_today(input()))