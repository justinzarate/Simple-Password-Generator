import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*"

while 1:
    password_len = int(input("How long would you like your password to be? "))
    password_count = int(input("How many passwords would you like to generate? "))
    for x in range(0, password_count):
        password = ""
        for y in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password : ", password)