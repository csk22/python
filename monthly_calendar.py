from datetime import datetime,timedelta
import calendar

class MyCalendar():
    def calculateMonth(self,*args):
        c = calendar.TextCalendar()
        st = c.formatmonth(args[1],args[0],0,0)
        print(st)

def main():
    c = MyCalendar()
    print("Enter Month:")
    month = input()
    print("Enter Year:")
    year = input()
    c.calculateMonth(int(month),int(year))

if __name__ == "__main__":
    main()