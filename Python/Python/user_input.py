# Validate User Input Exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username mus not contain digits

username = input("Enter a Username: ")

if len(username) > 12:
    print("Your username is to long! ")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
