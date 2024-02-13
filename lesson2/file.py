### read

# f = open("lesson2\demofile.txt", "r")
# print(f.read())
# f.close()

## create/write
# f = open("lesson2\demofile.txt", "w") ## or 'a'
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("lesson2\demofile.txt", "r")
# print(f.read())

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

### Delete File

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
