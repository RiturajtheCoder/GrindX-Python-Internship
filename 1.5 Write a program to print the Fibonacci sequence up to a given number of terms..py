#5. Write a program to print the Fibonacci sequence up to a given number of terms.
while True: #Infinite loop to repeatedly run the Fibonacci series calculation
    try: #Try block to handle potential exceptions
        n=int(input("\n\t Enter the number of terms for the Fibonacci series: ")) #Prompt the user to enter the number of terms for the Fibonacci series
        if(n<=0): #Check if the input is a positive integer
            print("\n\t Please enter a positive integer.") #Prompt to the user to input a valid number
        else: #If the number is greater than 0
            print(f"\n\t The first {n} terms of the Fibonacci series are:") #Prompt to print the fibonacci series
            a,b=0,1  #Initializing the first two terms of the Fibonacci series
            for i in range(n): #Loop to calculate and display `n` terms of the series
                print(a, end=" ") #Print the current term
                a, b=b,a+b #Update `a` and `b` to the next terms in the series
            print() #Print a newline for better formatting
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Please enter a valid integer.") #Inform the user to input a valid integer
