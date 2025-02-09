#2.1 Write a program to find the largest and smallest elements in a list.
while True: #Infinite loop to repeatedly run the Fibonacci series calculation
    try: #Try block to handle potential exceptions
        n=input("\n\t Enter the list : ").split() #Prompt to the user to enter the list elements
        f=[float(x) for x in n] #Converting the list to float data type
        print(f"\n\t The entered list is {f}") #Prompt to the user to show the list entered
        mi=min(f) #Command to find the smallest element in the list
        ma=max(f) #Command to find the larest element in the list
        print(f"\n\t The smallest element of list {f} is {mi}") #Prompt to print the smallest element in the list
        print(f"\n\t The largest element of list {f} is {ma}") #Prompt to print the largest element in the list
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Enter a number only !") #Prompt to the user to enter a number only

