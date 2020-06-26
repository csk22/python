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
            dates = []
            for week in cal:
                if week[day] != 0:
                    dates.append(week[day])
                        
            for d in dates:
                print("%10s %2d" %(calendar.month_name[m], d))

def main():
    print("Enter which day you want to schedule a meeting: ")
    day = input()
    m = Meeting()
    m.getdates(day)

if __name__ == "__main__":
    main()