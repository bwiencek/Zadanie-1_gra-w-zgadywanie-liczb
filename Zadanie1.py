#belowe python function will collect number from the User and forward it as a integer.
import random

def enter_number():
    while True:
        try:
            result = int(input("Please enter your number:"))
            break
        except ValueError:
            print("This is not a number - please enter number")

    return result

def computer_number():
    draw_number = random.randint(1, 100)
    user_number = enter_number()

    while user_number != draw_number:
        if draw_number < user_number:
            print("Too big!")

        elif draw_number > user_number:
            print("Too small!")

        else:
            print("You win!")

if __name__ == '__main__':
    guess_the_number()