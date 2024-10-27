import random
max_number = int(input("Enter the maximum number: "))
randomom_number :int  = random.randint(1, max_number)
print(f"random number is : {randomom_number}")


def gess_number():
    guess= int(input("enter the guess number: "))
    score =0
    if guess == randomom_number:
        score += 1    
        print("You have guessed the number")
    else:
        if randomom_number - guess < 7 and randomom_number - guess > 3 :
                print("you are close to the number")
        elif randomom_number - guess < 3:
            print("you are very close to the number")
        elif randomom_number - guess > 7 and randomom_number - guess < 14:
            print("you are far from the number")
        elif randomom_number - guess > 14:
            print("you are very far from the number")
            
        if score > 0 :        
            print(f"\nYour score is : , {score - 1}")

        else:
            print(" wrong answer You have 0 score")

        print("Try again")
    gess_number()
gess_number()