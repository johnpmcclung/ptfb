"""
if name is < 3 chars long
    name must be at least 3 chars
otherwise if its more than 50 char
    name must be less than 50 chars
otherwise
    name looks good
"""

def find_name():
    return input("Please enter your name: ")

name = find_name()

if len(name) < 3:
    print("Length of name must be at least 3 characters long!")
elif len(name) > 50:
    print("Length of name must no more than 50 characters long")
else:
    print("Name looks good! Move forward.")
