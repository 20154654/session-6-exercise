import sys
import random

# create random 10 letters password
num_charts = 10
if len(sys.argv)>1:
    num_charts=int(sys.argv[1])  #take number from user input in command line

    password = ""
    for index in range(num_charts):
        char_index = random.randint(0,25)
        char_index += ord('a')
        password += chr(char_index)

print(password)