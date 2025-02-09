#2.4 Develop a function to find the GCD (Greatest Common Divisor) and LCM (Least Common Multiple) of two numbers.
def gcd(a, b): #Defining a function to calculate the Greatest Common Divisor (GCD) of two numbers
    res = a if a < b else b #Initializing res to find the smallest of the two numbers
    while res > 0: #Looping until res becomes 0
        if a % res == 0 and b % res == 0: #Checking if res divides both a and b without a remainder
            break #If true, break out of the loop
        res -= 1 #Decrement res by 1 and check the next smaller number
    return res #Return the GCD value
def lcm(a, b): #Defining the function to calculate the Least Common Multiple (LCM) of two numbers
    l = (a * b) // gcd(a, b) #Use the formula LCM(a,b)=(a*b)/GCD(a,b)
    return l #Return the LCM value
while True: #Infinite loop to repeatedly take input from the user until manually stopped
    try:  #Try block to handle potential exceptions
        a = int(input("\n\t Enter the first number : ")) #Prompt to the user to input the first integer
        b = int(input("\n\t Enter the second number : ")) #Prompt to the user to input the second integer
        res1 = gcd(a, b) #Calling the gcd function to calculate the GCD of a and b
        res2 = lcm(a, b) #Calling the lcm function to calculate the LCM of a and b
        print(f"\n\t The GCD of {a} and {b} is : {res1}") #Print the calculated GCD
        print(f"\n\t The LCM of {a} and {b} is : {res2}") #Print the calculated LCM
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Enter a valid integer") #Inform the user to enter valid integers
