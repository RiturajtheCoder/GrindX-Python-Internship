#3.5 Write a program to simulate the behavior of a stack using lists, including push, pop, and peek operations.
#Stack class to simulate stack behavior using a list
class Stack:#Define the class 'Stack'
    def __init__(self):#defining a function to acces the variables or methods in the class
        #Initialize an empty list to represent the stack
        self.stack=[] #Initializing the stack to be empty
    #Push operation to add an element to the stack
    def push(self, item):
        #Append the item to the stack list
        self.stack.append(item) #Appending the entered item which is to be pushed
        print(f"\n\t Item '{item}' pushed to the stack.")  # Confirmation message for item push
    #Pop operation to remove and return the top element from the stack
    def pop(self): #Function to define pop function for a stack
        #Check if the stack is not empty
        if not self.empty(): #If the stack is not empty
            #Remove the last element from the stack (top item)
            popped=self.stack.pop() #Popped element
            #Print and return the popped item
            print(f"\n\t Item '{popped}' popped from the stack.") #Prompt to the user to show the piopped element
            return popped  #Return the popped element
        else: #If the stack is empty
            print("\n\t Error: Stack is empty. Cannot perform pop.")  #Error if stack is empty
            return None #Return nothing

    #Peek operation to view the top element of the stack without removing it
    def peek(self): #Function to peek into the stack
        #Check if the stack is not empty
        if not self.empty(): #If the stack is not empty
            #Access the last element of the stack (top item)
            top=self.stack[-1]  #The topelement
            print(f"\n\t Top item is: {top}")  #Display the top item
            return top  #Return the top element
        else: #If the stack is empty
            print("\n\t Error: Stack is empty. Cannot perform peek.")  #Error if stack is empty
            return None #Return Nothing
    #Check if the stack is empty
    def empty(self): #Function to check if the stack is empty or not
        #Return True if the stack is empty, otherwise False
        return len(self.stack)==0  #Returning the length of the stack
    #Display the current elements in the stack
    def display(self): #Function to shwo the stack element
        #Check if the stack is not empty
        if not self.empty(): #If the stack is not empty
            #Display the current elements in the stack
            print("\n\t Current stack elements: ", self.stack) #Prompt to the user to show the stack elements
        else: #If the stack is empty
            print("\n\t The stack is empty.")  #Error message if stack is empty
#Main program to test stack operations
if __name__ == "__main__": #Checking if it is the main program
    stack = Stack()  #Create an instance of the Stack class
    while True:  #Infinite loop for user input
        #Displaying the stack operations menu
        print("\n\t Stack Operations Menu")
        print("\n\t 1. Push")
        print("\t 2. Pop")
        print("\t 3. Peek")
        print("\t 4. Display Stack")
        print("\t 5. Exit")
        #Get the user's choice for an operation
        choice = input("\n\t Choose an option (1/2/3/4/5): ")
        #Perform the corresponding operation based on user input
        if(choice == '1'):  #Push operation
            item = input("\n\t Enter the item to push: ")  #Get item input
            stack.push(item)  #Call push method
        elif(choice == '2'):  #Pop operation
            stack.pop()  #Call pop method
        elif(choice=='3'):  #Peek operation
            stack.peek()  #Call peek method

        elif(choice=='4'):  #Display stack elements
            stack.display()  #Call display method
        elif (choice=='5'):  #Exit the program
            print("\n\t Exiting the program !")  #Confirmation message
            break  #Break the loop to exit the program
        else:  #Invalid input handling
            print("\n\t Invalid choice. Please choose a valid option.")  #Error message for invalid choice
            continue  #Continue prompting for valid input
