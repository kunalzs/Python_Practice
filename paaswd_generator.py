import string
import random

new_pass = ""
def passwd_generator(strength, pass_symbols, pass_numbers):
    
    global new_pass
    if pass_symbols == "y":
        if pass_numbers == "y":
            # new_pass = random_password with symbols and numbers
            password_characters = string.ascii_letters + string.digits + string.punctuation
            new_pass = ''.join(random.choice(password_characters)for i in range(strength))
            # print("Your new Password is: ", new_pass)
            return (new_pass)
        else :
            password_characters = string.ascii_letters + string.punctuation
            new_pass = ''.join(random.choice(password_characters)for i in range(strength))
            # print("Your new Password is: ", new_pass)
            return (new_pass)
    else:
        if pass_numbers == "y":
            password_characters = string.ascii_letters + string.digits
            new_pass = ''.join(random.choice(password_characters)for i in range(strength))
            # print("Your new Password is: ", new_pass)
            return (new_pass)
        else:
            password_characters = string.ascii_letters
            new_pass = ''.join(random.choice(password_characters)for i in range(strength))
            return (new_pass)

print("***Password Genrator***")
strength = int(input ("What will be your Password strength:"))
pass_symbols = input("Do you want symbols in your Password?, Type y/n:")
pass_numbers = input("Do you want numbers in your Password?, Type y/n:")
passwd_generator(strength,pass_symbols,pass_symbols)
print("Your new Password is: ", new_pass)