#below python program will collect number from the User and will draw a number by the computer and display a message if the user number is too small, too large or the same as the computer's..
import random

#function that will collect number from the User and forward it as a integer
def enter_number():
    while True:
        try:
            result = int(input("Please enter your number:"))
            break
        except ValueError:
            print("This is not a number - please enter number")

    return result

#function that will compare user's and computer's numbers and will display a massage.
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

#(poniższego nie rozumiem - do wyjaśnienia z Wykładowcą/Mentorem).
if __name__ == '__main__':
    guess_the_number()