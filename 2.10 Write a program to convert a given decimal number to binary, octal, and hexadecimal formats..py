#2.10 Write a program to convert a given decimal number to binary, octal, and hexadecimal formats.
while True: #Infinite loop to repeatedly run the program
    try: #Try block to handle potential exceptions
        dec=int(input("\n\t Enter the decimal number : ")) #Prompt to the user to enter a decimal number
        print(f"\n\t\t The decimal value of {dec} is : ") #Displaying the entered decimal number
        print(f"\n\t\t {bin(dec)} in Binary number system") #Converting the decimal number to binary and displaying the result
        print(f"\n\t\t {oct(dec)} in Octal number system") #Converting the decimal number to octal and displaying the result
        print(f"\n\t\t {hex(dec)} in Hexa-decimal number system") #Converting the decimal number to hexadecimal and displaying the result
    except ValueError: #Handling the case where the input is not a valid integer
        print("\n\t Enter a number belonging to the decimal numbering system !") #Displaying an error message if the input is invalid



