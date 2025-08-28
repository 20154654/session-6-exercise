
# data = """This is going to be a bunch of information that I am going to test. 
# Heading 1: used for testing purpose.
# Heading 2: not sure what i am doing.
# the end.
# """

# heading_1_index = data.find("Heading")
# print("index 1:", heading_1_index)
# heading_2_index = data.find("Heading",heading_1_index+1)   #start from previous heading+1 location
# print("index 2:", heading_2_index)
# print("heading1",data[heading_1_index:heading_2_index])  #print out the information between 

# heading_3_index = data.rfind("Heading")
# print("index 3:", heading_3_index)
# print("heading2",data[heading_3_index:])

# print(data.startswith("This"))


####################################
'''
Activity 1: String MagicActivity 1: String Magic
Objective: Write a program to perform basic operations on a string.
Instructions:
Create a string variable 
Ask user to input their name (Enter your name:)
Concatenation: Combine the string (user_name) with another string (how are you?)
Change Case: Convert the string (user_name) to uppercase.
Task: 
Run the code to see the output.
'''

# user_name = input("What's your name: ")
# user_name = user_name.strip()
# print(f"Hello {user_name}, how are you?")
# print(user_name.upper())


####################################
'''
Activity 2 Broken Keyboard
Time allocated:
30 minutes
Task
Scenario
Your friend's keyboard is broken, and cannot type the a, u, and e keys. This is very annoying, so the user includes the words not and poor sometimes in sentences.
 Step 1
The user types the following:
## in place of an a
i n p l a c e o f a u less than divided by l i greater than less than l i greater than$ in place of an e

Step 2
The broked keyboard frustrates your friend, and he often use not and bad in messages.   Find the words not and bad in the sentence and replace all the texts, between not and bad, including not and bad, with the word good.
Example
Input: The day was not that bad.
Output: The day was good
Summary
correct the message entered, and
that replace not.....bad with good.

Test if your program works:
Test case 1
Input: My k$$$ybo##rd is brok$$$n, b$$t l$$ckily th$$$ music on th$$$ r##dio is not th##t b##d. 
Output: My keyboard is broken, but luckily the music on the radio is good.

Test case 2
Input: The d##y ##t th$$$ b$$$##ch w##s not th##t b##d ##ft$$$r ##ll. 
Output: The day at the beach was good after all.
'''

origin_msg = input("Type your message: ")
origin_msg = origin_msg.strip()

replace_dict={
    "replace_from": ["$$$","##","$$"],
    "replace_to": ["e","a","u"]
}

new_msg = origin_msg
# fixing e/a/u input
for i in range(len(replace_dict["replace_from"])):
    # print(i, " Replacing ", replace_dict["replace_from"][i], "to", replace_dict["replace_to"][i])    
    new_msg = new_msg.replace(replace_dict["replace_from"][i], replace_dict["replace_to"][i])
    # print(new_msg)

# fixing not ... bad, with multiple check. This is case sensitive, so need to fix that too!
while new_msg.find("not") != -1 and new_msg.find("bad") != -1:
    start_index = new_msg.find("not")
    end_index = new_msg.find("bad", start_index+1)
    str_to_be_replace = new_msg[start_index:end_index+3]
    new_msg = new_msg.replace(str_to_be_replace, "good")

    if start_index == -1 or end_index == -1:
        print("start_idnex:", start_index, " end index: ", end_index)
        break


print(f"Original message is : {origin_msg}")
print(f"Fixed message is : {new_msg}")

