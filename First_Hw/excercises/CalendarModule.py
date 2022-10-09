import calendar

week=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
day=list(map(int,input().split()))
print(week[(calendar.weekday(day[2],day[0],day[1]))])
