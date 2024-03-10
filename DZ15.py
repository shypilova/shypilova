x = int(input())
d1 = ("день", "дні", "днів")
day = 86400
hour = 3600
days = x // day
hours = (x - days * day) // 3600
rest = (x - days * day) - hours * hour
minute = rest // 60
seconds = rest - minute * 60
my_dict = {"hours": hours, "minute": minute, "seconds": seconds}
if days % 10 == 1 and days % 100 != 11:
        a = d1[0]
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        a = d1[1]
else:
        a = d1[2]
print(days, a, ',', my_dict['hours'], ':', my_dict['minute'], ':', my_dict['seconds'])