#3.4 Create a function to merge two dictionaries and handle conflicts by summing the values of common keys.
def merge(d1, d2): #Creating a function to merge the two dictionaries
    #Create a copy of the first dictionary to avoid modifying the original
    merged = d1.copy() #Copying d1 to avoid modifying the original dictionary 
    #Iterate through the second dictionary
    for key, value in d2.items(): #Loop through each key-value pair in d2
        if key in merged:  #If the key from d2 is already in the merged dictionary
            #If the key exists, sum the values
            merged[key]+=value  #Adding the value from d2 to the value in merged
        else: #If key is not in merged
            #If the key does not exist, add it to the merged dictionary
            merged[key] = value  #Adding the new key-value pair to merged dictionary
    return merged  #Return the merged dictionary
def get(): #Creating a function to get the dictionary values
    #Prompt the user to enter a dictionary in the specified format
    u=input("\n\t Enter Dictionary (key=value,key=value): ")  #Prompt user for dictionary input in 'key=value' format
    pairs=u.split(',') #Split the input string by commas to separate key-value pairs
    u={}  #Initialize an empty dictionary
    for pair in pairs:  #Loop through each key-value pair string
        key, value=pair.split('=')  #Split each pair by the equal sign to separate key and value
        u[key.strip()] = float(value.strip())  #Convert the value to float and store in the dictionary, strip removes leading/trailing whitespaces
    return u  #Return the created dictionary
while True:  #Infinite loop to allow continuous dictionary merging
    try: #Try block to handle exceptions
        print("\n\t Merging two dictionaries")  #Print message indicating the action
        d1=get()  #Get the first dictionary from user input
        print(f"\n\t First Dictionary: {d1}")  #Print the first dictionary
        d2=get()  #Get the second dictionary from user input
        print(f"\n\t Second Dictionary: {d2}")  #Print the second dictionary
        res=merge(d1, d2)  #Call the merge function to merge the two dictionaries
        print(f"\n\t Merged Dictionary: {res}")  #Print the merged dictionary
    except ValueError:  #Catch ValueError in case of invalid input (e.g., non-numeric value for dictionary)
        print("\n\t Enter a numerical value for the dictionary")  #Error message for invalid numerical input
    except Exception as e:  #Catch any other unforeseen exceptions
        print(f"\n\t An error occurred: {e}")  #Print the error message


