#3.1 Create a program to solve a quadratic equation and display the real roots (if any).
import math #Importing math module for square root function
while True: #Infinite loop to allow multiple calculations
    try: #Try block to handle potential exceptions
        print("\n\t Quadratic Equation : ax^2+bx+c=0") #Displaying the general form of a quadratic equation
        a=float(input("\n\t Enter coefficient a : ")) #Taking input for coefficient 'a'
        if(a==0): #Checking if the equation is truly quadratic
            print("\n\t If 'a' is zero then the equation isn't a quadratic equation ") #If 'a' is zero, it's not a quadratic equation
            continue #Restarting the loop to ask for a valid 'a' value
        b=float(input("\n\t Enter coefficient b : ")) #Taking input for coefficient 'b'
        c=float(input("\n\t Enter coefficient c : ")) #Taking input for coefficient 'c'
        d=(b**2)-(4*a*c) #Calculating the discriminant (D = b² - 4ac)
        #Checking the nature of roots based on the discriminant value
        if(d>0): #If D > 0, there are two distinct real roots
            r1=(-b+math.sqrt(d))/(2*a) #Calculating first root
            r2=(-b-math.sqrt(d))/(2*a) #Calculating second root
            print(f"\n\t The two real roots are {r1:.2f} and {r2:.2f}") #Displaying the real roots
        elif(d==0):#If D == 0, there is exactly one real root
            r=(-b/(2*a)) #Calculating the root
            print(f"\n\t The one real root is {r:.2f}") #Displaying the single real root
        else: #If D < 0, no real roots exist (complex roots exist)
            print("\n\t No real roots exists(complex roots exists)") #Displaying there are no roots
    except ValueError: #Handling cases where input is not a valid number
        print("\n\t Enter valid numerical values") #Prompting the user to enter only numbers
