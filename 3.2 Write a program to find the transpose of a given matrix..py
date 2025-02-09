#3.2 Write a program to find the transpose of a given matrix.
while True: #Infinite loop to allow multiple calculations
    rows=int(input("\n\t Enter the number of rows : ")) #Taking user input for number of rows
    cols=int(input("\n\t Enter the number of columns : ")) #Taking user input for number of columns
    mat=[] #Initializing an empty list to store the matrix
    print("\n\t Enter the elements row-wise(alphanumeric values allowed) : ") #Prompting the user to enter matrix elements row-wise
    for i in range(rows): #Iterating over the number of rows
        while True: #Looping until the user provides correct input
            row=input(f"\n\t Row {i+1} : ").split() #Taking row input and splitting it into list elements
            if(len(row)!=cols): #Checking if the number of inputs matches the specified number of columns
                print(f"\n\t Invalid input! Please enter exactly {cols} numbers") #Error message for incorrect input
                continue #Restarting the loop to take correct input
            else: #If length of rows is equal to that of column's
                mat.append(row) ##Appending the valid row to the matrix
                break #Breaking the loop to move to the next row
    print("\n\t Orginal Matrix : ") #Displaying the original matrix
    for row in mat: #Iterating through each row of the matrix
        print(f"\n\t {row}") #Printing the row
    tran=[[mat[j][i] for j in range(rows)] for i in range(cols)] #Generating the transpose of the matrix using list comprehension
    print("\n\t Transposed Matrix : ") #Displaying the transposed matrix
    for row in tran: #Iterating through each row of the transposed matrix
        print(f"\n\t {row}") #Printing the row
