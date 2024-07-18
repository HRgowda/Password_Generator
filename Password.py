# Importing the required modules
import random 
import string

# Defining character sets for generating random strings
alpha = string.ascii_letters  # Contains all upper and lower case letters
num = string.digits            # Contains all numerical digits
special = string.punctuation   # Contains special characters like !, @, #, etc.

# Defining lengths for different parts of the final string
length1 = 4  # Length of the random letters portion
length2 = 3  # Length of the random digits portion
length3 = 2  # Length of the random special characters portion

# Initializing empty strings to store generated characters
alphabets = ''
numbers = ''
special_characters = ''

# Generating random letters
for _ in range(length1):
    alphabets += random.choice(alpha)

# Generating random digits
for _ in range(length2):
    numbers += random.choice(num)

# Generating random special characters
for _ in range(length3):
    special_characters += random.choice(special)

# Combining the generated parts to form the final string
password = alphabets + str(numbers) + str(special_characters)

# Printing the final random string
print("The generated password is: ",password)
