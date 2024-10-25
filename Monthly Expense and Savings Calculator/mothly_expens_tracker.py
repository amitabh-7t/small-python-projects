def expenses() -> None: 
    num : int = int(input("enter the number of categories: "))
    for _ in range(num):
        key = input(f"Enter the {_+1} category name: ")
        value = input("Enter the category expense : ")
        userdict[key] = value

    
    global sum  
    sum = 0
    print("------------------------------------")
    for key in userdict:
        sum = sum + int(userdict[key]) 
    print(f"\nyour total expense is : {currency} {sum}\n") 
    print("------------------------------------")

def calculation(monthly_salary,tax,currency,xpens_sum) -> None:
    monthly_salary_after_tax = monthly_salary - (monthly_salary * (tax/100))
    savings = monthly_salary - xpens_sum
    print(f"\nyour monthly salary \n  after tax : {currency} {monthly_salary_after_tax}\
            \n  total savings: {currency} {savings}.\n")
    yearlysalarat = monthly_salary_after_tax *12
    yearlysalar = monthly_salary *12
    print("------------------------------------")

    print(f"\nyour yearly salary\n  before tax {currency} {yearlysalar}\
          \n  after tax : {currency} {yearlysalarat}\n")
    print("------------------------------------")



    

def main()-> None:
    
    global userdict 
    global monthly_salary
    global tax
    global currency

    userdict = {} 
    currency = input("enter the currency: ")
    monthly_salary = float(input("enter your monthly salary : "))
    tax = float(input("enter tax (%): "))
    expenses()
    calculation(monthly_salary,tax,currency,sum)

main()