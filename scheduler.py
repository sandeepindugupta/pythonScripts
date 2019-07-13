import calendar
# change these values to your needs ...
import datetime
import subprocess
now = datetime.datetime.now()
# print(str(now.date()))
# print(type(str(now.date())))
year = now.year
now1=f"{datetime.datetime.now():%m-%d-%Y}"
print(now1)
# print(type(now1))
# be nice
# days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
# print("All first workdays of each month in %d:" % year)
# go 3 days into each month in case it starts with Saturday, Sunday
sf2=[]
# print(type(sf2))
for ix, month in enumerate(range(1, 13)):
    for day in range(1, 4):
        weekday = calendar.weekday(year, month, day)
        if weekday < calendar.SATURDAY:
            # format the result
            sf = "%02d-%02d-%d"
            
            sf1=sf % ( month, day, year)

            sf2.append(sf1)
            # print(sf % ( month, day, year))

            break
 
for check in sf2:
  if(now1==check):
    print("execute")
    break
  else:
    
    subprocess.call(" python test.py", shell=True)
    print("not execute")
    break
  
  # print(check)