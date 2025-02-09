#1.4 Develop a function to check if a given string is a palindrome.
def palindrome(n): #Defining a function to check if a number is a palindrome
    rev=0 #Initializing the variable to store the reversed number
    temp=n #Creating a temporary copy of the input number `n`
    while(temp!=0): #Looping until the temporary number becomes 0
        rev=rev*10+temp%10 #Extracting the last digit of `temp` and add it to `rev`
        temp//=10 #Removing the last digit from `temp` by integer division
    return rev==n #Returning True if the reversed number equals the original number, otherwise False
while True: #Infinite loop to keep prompting the user for input until manually stopped
    try: #Try block to handle invalid inputs
        n=int(input("\n\t Enter a numnber : ")) #Prompt the user to input a number and convert it to an integer
        res=palindrome(n) #Calling the `palindrome` function to check if the input number is a palindrome
        if(res): #If the result is True
            print(f"\n\t {n} is a palindrome") #Print that the number is a palindrome
        else: #If the result is False
            print(f"\n\t {n} is not a palindrome") #Print that the number is not a palindrome
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Enter a valid integer") #Inform the user to enter a valid integer
