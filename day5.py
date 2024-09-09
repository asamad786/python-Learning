import random
import string

print("=======================================================")   


'''
FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''


# for number in range(0, 101):
#     if number%3 == 0 and number%5 == 0:
#         print("FizzBuzz")
#     elif number%3 == 0:
#         print("Fizz")
#     elif number%5 == 0:
#         print("Buzz")00000000
#     else:
#         print(number)

print("=======================================================")   

'''
Create a Password Generator
'''

# letters = [letter for letter in string.ascii_lowercase] + [letter for letter in string.ascii_uppercase]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']      
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',] 
symbols = ['!', '@', '#', '$', '%', '^', '*']

# print(letters)
# print(numbers)
# print(symbols)

print("Create Password")

get_letters = int(input("How many letters"))
get_numbers = int(input("How many numbers"))
get_symbol = int(input("How many Symbol"))
# get_generated_type = input("Enter Generated Type 1 for Easy and 2 for Hard")



# EASY PASSWOD
# password = ""


# for char in range(1, get_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for char in range(1, get_numbers + 1):
#     random_char = random.choice(numbers)
#     password += random_char

# for char in range(1, get_symbol + 1):
#     random_char = random.choice(symbols)
#     password += random_char

# print(password)



# HARD PASSWORD
password_list = []
for char in range(1, get_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, get_numbers + 1):
     password_list.append(random.choice(numbers))

for char in range(1, get_symbol + 1):
     password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
     password += char


print(password)