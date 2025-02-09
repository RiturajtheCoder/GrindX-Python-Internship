#1. Write a program to check if a number is even or odd.
while True: #To run the code as many times as needed
    try: #Try block to handle potential exceptions
        num=int(input("\n\t Enter a number : ")) #To take the input
        if(num%2==0): #To check if the number is divisible by two(i.e. the number is even if divisible)
            print(f"\n\t The number {num} is an even number ") #To print the output if the number is even
        elif(num%2!=0): #To check if the number is divisible by two(i.e. the number is odd if not divisible)
            print(f"\n\t The number {num} is an odd number") #To print the output if the number is odd
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Enter a valid integer value ") #Prompt the user to enter a valid integer
        
