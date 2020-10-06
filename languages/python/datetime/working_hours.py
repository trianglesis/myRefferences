import datetime

now = datetime.datetime.now().replace(second=0, microsecond=0)
morning = now.replace(hour=7)
evening = now.replace(hour=19)

print(f'Dates: {morning} - {now} - {evening}')

print(f'now > morning = {now > morning}')
print(f'now < morning = {now < morning}')
print(f'morning > now = {morning > now}')
print(f'morning < now = {morning < now}')

print(f'now > evening = {now > evening}')
print(f'now < evening = {now < evening}')
print(f'evening > now = {evening > now}')
print(f'evening < now = {evening < now}')

print(f'now - evening = {evening - now}')  # 17 hours day end = 0:00:00, 18 = 1:00:00

if now > morning and now < evening:
    print("Staring working hours!")
else:
    print("Working hours no more!")