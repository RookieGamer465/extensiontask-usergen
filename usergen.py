# extension task
# charley mckay

# gather information from user, change string to full capitals
firstname = str.upper(input("please enter your first name: "))
surname = str.upper(input("please enter your second name: "))

# construct the username with the given and calculated information
username = str(ord(firstname[0:1]))+str(ord(surname[-1:]))+firstname[0:5]+surname[0:5]+str(ord(surname[0:1]))
print(f"your generated username is: {username}")
