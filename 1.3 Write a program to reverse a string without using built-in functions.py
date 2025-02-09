#3. Write a program to reverse a string without using built-in functions.
while True: #Infinite loop to repeatedly ask for input
    s=input("\n\t Enter a string to reverse: ") #Prompt the user to input a string
    rev="" #Initialize an empty string to store the reversed string
    for i in range(len(s)-1,-1,-1): #Iterate through the original string in reverse order
        rev+=s[i]  #Append each character to the reversed string
    print(f"\n\t The reverse of the string '{s}' is: '{rev}'") #Print the original and reversed strings


