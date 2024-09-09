import random

print("=======================================================")      

user_choice = int(input("What do you Choose? 0 for Rock, 1 for Paper and 2 for Scissor"))
print(f"User Choise {user_choice}")


computer_choice = random.randint(0,2)
print(f"Computer Choise {computer_choice}")


if user_choice >= 3 or user_choice < 0:
    print("Please select valid nummber")

elif user_choice == 0 and computer_choice == 2:
    print("User Win")

elif computer_choice == 0 and user_choice == 2:
    print("Computer Win")

elif computer_choice > user_choice:
    print("Computer Win")

elif user_choice > computer_choice:
    print("User Win")

elif user_choice == computer_choice:
    print("Draw")

