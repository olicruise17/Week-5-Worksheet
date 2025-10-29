# Task: Reverse the text on each line of a file and save it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read each line.
# - Reverse the text of each line word by word -> 'hello my name is george' -> 'george is name my hello'
# - Write the reversed lines into a new file - the output file name should be the input filename + _reverse.txt
# for example: 'story.txt' -> 'story.txt_reverse.txt'

name = input("Enter file name: ")

with open(name+".txt","r") as infile:

    lines = infile.readlines()

    for line in lines:

        data = line.split(" ")
        reversed_data = data[::-1]

        reversed_data = " ".join(reversed_data)

        with open(name+"_reverse.txt","a") as reversed_file:

            reversed_file.write(reversed_data)
