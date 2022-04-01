import random
import string
from pathlib import Path
pwdNums = string.ascii_lowercase + string.ascii_uppercase + \
    string.digits + "@%+\\/'!#$^?:,(){}[]~"

username = input("Enter your username associated with the password: ")
length = int(input('Enter the password length: '))


temp = random.sample(pwdNums, length)
password = "".join(temp)
print(password)

user = username + ": " + password

if Path('generatedpwds.txt').is_file():
    with open('generatedpwds.txt', mode='a') as file:
        file.write(user + "\n")
else:
    with open('generatedpwds.txt', mode='w') as file:
        file.write(user + "\n")