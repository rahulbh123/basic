year=int(input("enter year"))
if (year%4==0 and year%100!=0 or year%40==0):
print("the year is leap year")
else:
print("year is not leap year")
