#2.5 Create a function to remove duplicate elements from a list while maintaining the order.
def remove_duplicates(lst): #Defining a function to remove the duplicates from a list
    unique_list=[] #Creating an empty list to store unique elements
    for item in lst: #Iterating through the given list
        if item not in unique_list: #Adding the item only if it's not already in unique_list
            unique_list.append(item)
    return unique_list #Returning the filtered list
#Driver code
while True: #Infinite loop to repeatedly run the program
    try: #Try block to handle potential exceptions
        lst = input("\n\t Enter the list of elements : ").split()#Taking input from the user
        numbers = [float(x) for x in lst] #Converting input values to float (optional, remove if dealing with strings)
        unique_sorted_list = remove_duplicates(numbers) #Calling the function
        print("\n\t List after removing duplicates:", unique_sorted_list) #Printing the result
    except ValueError: ##Handling the case where the input is not a valid integer
        print("\n\t Enter valid numbers only! ") #Prompt to the user to enter a number only


