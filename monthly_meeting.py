import calendar
from datetime import datetime

class Meeting():
    def getdates(self,*args):
        # c = calendar.monthcalendar(calendar.year)
        now = datetime.now()
        days = ['mon','tue','wed','thu','fri','sat','sun']
        val = str(args[0]).lower()
        day = days.index(val[:3])
        # print("day is ",day)
        year = int(now.strftime("%Y"))
        for m in range(1,13):
            cal = calendar.monthcalendar(year,m)
            weekone = cal[0]
            weektwo = cal[1]
            if weekone[day] != 0:
                meetday = weekone[day]
            else:
                meetday = weektwo[day]
            print("%10s %2d" %(calendar.month_name[m], meetday))

def main():
    print("Enter which day you want to schedule a meeting: ")
    day = input()
    m = Meeting()
    m.getdates(day)

if __name__ == "__main__":
    main()