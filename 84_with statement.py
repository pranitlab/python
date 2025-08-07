f = open("file.txt")
print(f.read())
f.close()

#same can be written with the statement like this:

with open("file.txt") as f:
    print(f.read)
    
#you dont have to close the file explicitly