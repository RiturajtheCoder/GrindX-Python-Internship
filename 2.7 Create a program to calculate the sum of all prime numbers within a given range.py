#2.7 Create a program to calculate the sum of all prime numbers within a given range
def is_prime(n): #Defining a function to check if a number is prime
    if n<2: #Checking if the number is less than 2 since prime numbers start from 2
        return False #Returning False as numbers less than 2 are not prime
    for i in range(2, int(n**0.5)+1): #Iterating from 2 to the square root of n for efficiency
        if n%i==0: #Checking if n is divisible by any number in the range
            return False #Returning False if a factor is found
    return True #Returning True if no factors are found, confirming the number is prime
def sum_of_primes(start,end): #Defining a function to calculate the sum of prime numbers in a range
    total=0 #Initializing a variable to store the sum of prime numbers
    for num in range(start,end+1): #Iterating through the given range
        if is_prime(num): #Checking if the current number is prime
            total+=num #Adding the prime number to the total sum
    return total#Returning the final sum of prime numbers
while True: #Infinite loop to repeatedly run the program
    try: #Try block to handle potential exceptions
        start=int(input("\n\t Enter the starting number : ")) #Prompting the user to enter the starting number
        end=int(input("\n\t Enter the ending number : ")) #Prompting the user to enter the ending number
        result=sum_of_primes(start,end) #Calling the function to calculate the sum of prime numbers in the range
        print("\n\t Sum of prime numbers in the range : ",result) #Printing the final sum
    except ValueError: #Handling the case where the input is not a valid integer
        print("\n\t Enter valid integer values ") #Prompting the user to enter valid integers


