# Task: Open a file and calculate the total number of lines, words, and characters.

# Instructions:
# - get the file name from the user
# - Read the file contents.
# - Count how many lines, words, and characters are in the file.
# - Print out the totals for each.

name = input("Enter file name: ")
number_words = 0

with open(name+".txt","r") as infile:


    lines = infile.readlines()
    number_lines = len(lines)

    for line in lines:
        words = line.split(" ")
        number = len(words)
        number_words += number




print(f"Lines: {number_lines}")
print(f"Words: {number_words}")
print(f"Characters: {number_characters}")



    