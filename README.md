# Simple-Password-Generator

**Description:**
> This is a simple password generator script written in Python. It allows users to generate random passwords based on their desired length and quantity.

**How to Use:**
> Run the script.
> When prompted, enter the desired length of your password.
> Next, specify how many passwords you'd like to generate.
> The script will then display the generated passwords.

**Features:**
> Allows users to specify password length.
> Allows users to specify the number of passwords to generate.
> Uses a combination of uppercase letters, lowercase letters, numbers, and special characters for password generation.

**Code**
```python
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
```
**Notes**
> Ensure you have Python installed on your machine to run the script.
> It's always recommended to use a combination of generated passwords and personal modifications to enhance security.
