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










