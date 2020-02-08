from datetime import datetime

print(str(datetime.now())[:10].replace('-', ':'))
print(datetime.now())

t = datetime.now()
print(t, t.date(), t.day, t.month)

