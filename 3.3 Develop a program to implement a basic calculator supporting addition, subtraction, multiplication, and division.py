#3.3 Develop a program to implement a basic calculator supporting addition, subtraction, multiplication, and division
while True:  #Starting an infinite loop to allow multiple calculations
    try: #Try block to handle potential exceptions
        print("\n\t Basic Calculator")  #Displaying the calculator heading
        num1=float(input("\n\t Enter first number : "))  #Taking the first number as input
        op=input("\n\t Enter an operator (+, -, *, /) : ")  #Taking the operator as input
        num2=float(input("\n\t Enter second number : "))  #Taking the second number as input
        #Performing the calculation based on the operator entered
        if(op=='+'):  #Checking if the operator is addition
            result=num1+num2  #Performing addition
            print(f"\n\t Result: {num1} + {num2} = {result}")  #Displaying the result
        elif(op=='-'):  #Checking if the operator is subtraction
            result=num1-num2  #Performing subtraction
            print(f"\n\t Result: {num1} - {num2} = {result}")  #Displaying the result
        elif(op=='*'):  #Checking if the operator is multiplication
            result=num1*num2  #Performing multiplication
            print(f"\n\t Result: {num1} * {num2} = {result}")  #Displaying the result
        elif(op=='/'):  #Checking if the operator is division
            if(num2==0):  #Checking for division by zero
                print("\n\t Error! Division by zero is not allowed.")  #Displaying error message
            else: #if the denominator is not 0
                result=num1/num2  #Performing division
                print(f"\n\t Result: {num1} / {num2} = {result}")  #Displaying the result

        else:  #Handling invalid operator input
            print("\n\t Invalid operator! Please enter one of +, -, *, /.")  #Displaying error message
    except ValueError:  #Handling invalid numerical input
        print("\n\t Error! Please enter valid numerical values.") #Displaying error message
        continue
    #Asking the user if they want to perform another calculation
    c=input("\n\t Do you want to perform another calculation? (yes/no): ").lower()  #Taking user input
    if(c!='yes'):  #Checking if the user wants to exit
        print("\n\t Exiting Calculator. Goodbye!")  #Displaying exit message
        break  #Exiting the loop if the user chooses not to continue
