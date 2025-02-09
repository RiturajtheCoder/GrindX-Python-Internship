#2.8 Write a function to generate a random password of a given length with alphanumeric characters.
import random #Importing the random module to generate random values
import string #Importing the string module to access letters and digits
def generate_password(length):#Defining a function to generate a random password
    characters=string.ascii_letters+string.digits#Combining uppercase, lowercase letters, and digits
    password="".join(random.choices(characters,k=length))#Generating a password by randomly selecting characters
    return password#Returning the generated password
while True: #Infinite loop to repeatedly run the program
    try: #Trying to handle potential exceptions
        length=int(input("\n\t Enter the desired password length : "))#Prompting the user to enter the password length
        if length<=0:#Checking if the entered length is valid
            print("\n\t Enter a positive integer for password length! ")#Prompting the user to enter a valid positive number
        else:#Executing if the entered length is valid
            print("\n\tGenerated Password:",generate_password(length))#Calling the function and printing the generated password
    except ValueError:#Handling the case where the input is not a valid integer
        print("\n\tEnter a valid integer value! ")#Prompting the user to enter a valid integer
