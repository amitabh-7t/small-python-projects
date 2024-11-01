def expense_splitter(no_of_people, price):
    total_expense = price
    split_expense = total_expense / no_of_people
    return split_expense

def main():
    while True:  # Loop until valid inputs are given
        try:
            no_of_people = int(input("Enter the number of persons: "))
            price = float(input("Enter the total expense: "))
            currency = "INR"
            distribution ={}
            total_sum=0
            print("enter the split percentage for ")
            for distri in range(no_of_people) :
                key = distri
                value = float(input(f"person {distri+1} :"))
                value = price * (value/100)
                distribution[key] = value
                total_sum = total_sum + value

            print("----- - -- --- -- - -----")
            if total_sum == price :
                for key, value in distribution.items():
                    print(f"person {key+1} will pay {currency} {value} ")  # Prints each key-value pair
            else :
                    print("distribution is not corect")

            print("----- - -- --- -- - -----")

            # print(f"Per person expense: {currency} {expense_splitter(no_of_people, price)}")
            break  # Break the loop if no exception occurs
        except ZeroDivisionError:
            print("Error: Number of people cannot be zero. Please enter a valid number.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
        
# Start the program
main()
