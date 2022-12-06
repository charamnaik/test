# Python program to check if given mobile number is valid

import re
def isValid(s):

    Pattern = re.compile("^([+]?)(\\d{3}[- .]?){2}\\d{4}$")
    return Pattern.match(s)

s = input("enter the contact number"+" ")
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")
