# validated who clean up the data
import re
email = input("whats your email? ").strip()

if re.search("^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")

else:
    print("invalid")

#youd can exclude the character

# alpha numeric pattern  \w =  word character or alphanumeric and underscore

# libraries are your friend

# validate input  that are data import  re.match, re.fullmatch start end of the string taken care





