#2.6 Write a program to check if a number is prime or not.
while True: #Infinite loop to repeatedly run the program
    try: #Try block to handle potential exceptions
        num=int(input("\n\t Enter a number : ")) #Prompt to the user to enter the number
        if(num>1): #Checking if the number is greater than 1 because prime numbers are greater than 1
            for i in range(2,(num//2)+1): #Iterating from 2 to half of the number to check for factors
                if((num % i)==0): #Checking if the number is divisible by any number in the range
                    print("\n\t",num,"is not a prime number") #Prompt to the user that the number is not prime if a factor is found
                    break #Breaking out of the loop as the number is confirmed non-prime
            else: #Executing when the loop completes without finding a factor
                print("\n\t",num,"is a prime number") #Prompt to the user that the number is prime
        else: #Executing if the number is 1 or less
            print("\n\t",num,"is not a prime number") #Prompt to the user that the number is not prime
    except ValueError:#Handle the case where the input is not a valid integer
        print("\n\t Enter a integer value ") #Prompt to the user to enter an integer value only
