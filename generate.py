import random
import string
from pathlib import Path
pwdNums = string.ascii_lowercase + string.ascii_uppercase + \
    string.digits + "@%+\\/'!#$^?:,(){}[]~"

while True:
    username = input("Enter your username associated with the password: ")
    if len(username) < 1:
        print("A username must be associated with the password.")
        continue
    else:
        break

website = input("Enter associated website (optional): ")

while True:
    length = input('Enter the password length: ')
    if len(length) < 1:
        print("Password length must be greater then 0.")
        continue
    else:
        break

temp = random.sample(pwdNums, int(length))
password = "".join(temp)
print(password)

user = username + ": " + password
userLog = f"{username}@{website}: {password}"

if Path('generatedpwds.txt').is_file():
    with open('generatedpwds.txt', mode='a') as file:
        if len(website) > 0:
            file.write(userLog + "\n")
        else:
            file.write(user + "\n")
else:
    with open('generatedpwds.txt', mode='w') as file:
        if len(website) > 0:
            file.write(userLog + "\n")
        else:
            file.write(user + "\n")
