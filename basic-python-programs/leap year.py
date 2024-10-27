#7. Develop a Python program to check if a given year is a leap year.
def inputed():
    global year
    year= int(input("year: "))
    is_leap_year(year)
def is_leap_year(year):
    if year%100!=0  and year%4==0 or year%400==0 :
            print(year," : is a leap year")
    else:
        print(year," : is not a leap year")
    inputed()
            

inputed()