# w = writing
# a = appending
# r = reading
# r+ = reading/writing

# file = open("./data.csv", "w")
# file = open("./data.csv", "r+") #reading and writing
# file = open("./data.csv", "r+") #reading and writing
# print(file.read())

# for line in file:
#     print(line)

# print(file.readlines())

# file.write("id,nam
# e,email\n")
# file.write("1,jes,tes@gmail.com\n")
# file.write("3,tetttx,tes222@gmail.com\n")
# file.close()


#best practice, to check whether file is existing or not
import os.path

filename = "data.csv"
if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")
