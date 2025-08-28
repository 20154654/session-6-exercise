import random

# create random 10 letters password
num_charts = 10
password = ""
for index in range(num_charts):
    char_index = random.randint(0,25)
    char_index += ord('a')
    password += chr(char_index)

print(password)