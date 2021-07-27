# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
MM,DD,YYYY=map(int,input().split(" "))
day={0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
print(day[calendar.weekday(YYYY,MM,DD)])