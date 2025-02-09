#2. Create a function to calculate the factorial of a given number.
def fac(n): #Defining the function to calculate the factorial of a number
    if(n<0): #To Check if the number is negative or not
        return "Factorial of negative numbers doesn't exist" #Returning message for negative numbers
    if(n==0 or n==1): #To Check if the number is 0 or 1(as factorial of both is 1)
        return 1 #Returning 1 if the enetered number is 0 or 1
    else: #If the number greater than 1
        f=1 #Initializing the factorial variable to 1
        for i in range(1,n+1): #Looping from 1 to n (inclusive)
            f*=i #Multiplying f by the current value of i
        return f #Returning the calculated factorial
while True: #To run the code as many times as needed
    try: #Try block to handle potential exceptions
        num=int(input("\n\t Enter a number : "))
        res=fac(num) #Calling the `fac` function to calculate the factorial of the input number
        print(f"\n\t The factorial of {num} is {res}") #Print the factorial result
    except ValueError: #Handling the case where the input is not a valid integer
        print("\n\t Enter a valid integer") #Prompt the user to enter a valid integer
