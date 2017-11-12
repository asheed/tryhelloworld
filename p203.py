days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for k in days_in_month:
    print(k)

for k, v in days_in_month.items():
    print("{}은 {}일이 있습니다.".format(k, v))

for k in days_in_month:
    print("{}은 {}일이 있습니다.".format(k, days_in_month[k]))



