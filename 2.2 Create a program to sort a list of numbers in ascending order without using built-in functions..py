#2.2 Create a program to sort a list of numbers in ascending order without using built-in functions.
while True: #Infinite loop to repeatedly run the Fibonacci series calculation
    try: #Try block to handle potential exceptions
        l=input("\n\t Enter the list : ").split() #Prompt to the user to enter the list elements
        f=[float(x) for x in l] #Converting the list to float data type
        print("\n\t Entered List : ",f) #Prompt to the user to show the list entered
        #Implements a nested loop to perform a manual sorting of the list (ascending order)
        for i in range(0, len(f)): #Iterates through each element of the list
            for j in range(i+1, len(f)): #Comparing the current element with all subsequent elements
                if(f[i]>=f[j]): #Checking if the current element is greater than or equal to the compared element
                    f[i],f[j]=f[j],f[i] #Swapping the elements if the condition is true
        print("\n\t Sorted List",f) #Prompt to the user to show the sorted list
    except ValueError: #Handle the case where the input is not a valid integer
        print("\n\t Enter a number !") #Prompt to the user to enter a number only
