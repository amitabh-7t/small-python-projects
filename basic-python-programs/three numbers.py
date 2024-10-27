#8. Create a Python program to determine the largest among three numbers entered by the user.
first_number= int(input("enter first number : "))
second_number= int(input("enter second number : "))
third_number = int(input("enter third number : "))

if first_number > second_number and first_number > third_number :
    print("first number ",first_number)

elif second_number >first_number and second_number > third_number :
    print("second number ",second_number)

elif third_number >first_number and third_number > second_number :
    print("third number ",third_number)

elif first_number == third_number or third_number == second_number or first_number== second_number:

    if first_number > second_number or first_number> third_number:
        print("first number ",first_number)

    elif second_number >first_number or second_number > third_number:
        print("second number ",second_number)

    elif third_number >first_number or third_number> second_number:
        print("third number ",third_number)

    elif first_number == third_number == second_number :
        print("All are equal",third_number)