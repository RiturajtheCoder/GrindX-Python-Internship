#2.3 Write a program to count the occurrences of each word in a given string.
string = "HELLO WORLD" #Input string
word = "HELLO" #Word to count
words_list = string.split(" ") #Split the string by spaces into a list
count = 0 #Initialize a counter to 0
for w in words_list: #Loop through each word in the list
    if w == word: #If the word matches the target word, increment the counter
        count += 1 #If the statement is true then increase the count by one each time
print(f"The word '{word}' occurs {count} time(s) in the given string.") #Print the number of occurrences
