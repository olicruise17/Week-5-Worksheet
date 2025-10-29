# Task: Create an exact copy of a file by reading its content and writing it to a new file.


# Instructions:
# - get the file name from the user
# - Open the original file and read its content.
# - Create a new file, and write the same content into it - the output file should be the input file name + _copy.txt
# e.g. story.txt -> story.txt_copy.txt

# Tip: Consider which file modes will let you read and write text data.

name = input("Enter file name:  ")

try:
    with open(name+".txt","r") as infile:

        content = infile.read()

    new_name = name + "_copy.txt"

    with open(new_name,"w")  as newfile:
        newfile.write(content)

    print("File Sucessfully Copied!")

except:
    print("File not found!")
    
