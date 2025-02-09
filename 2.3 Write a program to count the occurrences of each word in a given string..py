#2.3 Write a program to count the occurrences of each word in a given string.
# Python program to count the number of occurrences of a word in a given string

# Input string
string = "GeeksforGeeks A computer science portal for geeks"

# Word to count
word = "portal"

# Split the string by spaces into a list
words_list = string.split(" ")

# Initialize a counter to 0
count = 0

# Loop through each word in the list
for w in words_list:
    # If the word matches the target word, increment the counter
    if w == word:
        count += 1

# Print the number of occurrences
print(f"The word '{word}' occurs {count} time(s) in the given string.")
