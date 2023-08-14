from datetime import datetime
from datetime import date

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().time())
print(date.today())


#format
now = datetime.now()

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))

print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))

print(date.today().strftime("%d/%m/%Y"))
