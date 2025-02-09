#2.9 Develop a program to find the second largest element in a list.
while True: #Has started an infinite loop to repeatedly execute the program
    try: #Try block to handle potential exceptions
        l=input("\n\t Enter the numbers : ").split() #Taking space-separated numbers as input from the user
        f=[float(x) for x in l] #Converting the input values to a list of floats
        if(len(f)<2): #Checking if the list has at least two elements
            print("\n\t Enter atleast 2 items in thelist ") #Displaying a message to the user if the list has less than two elements
            continue #Restarting the loop if not enough numbers are provided
        print(f"\n\t Entered list : {f}") #Displaying the original unsorted list
        f.sort(reverse=True) #Sorting the list in descending order
        print(f"\n\t The second largest number in the list is {f[1]}") #Prompt to the user for showing the second largest number in the list
    except ValueError: #Handling the case where input is not a valid number
        print("\n\t Enter a proper numerical value! ") #Prompt to the user to enter a valid numerical value


