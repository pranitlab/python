with open("log.txt") as f:
    content = f.read()
    
if ("python " in content):
    print("yes python is present in the string")
    
else:
     print("yes python is not present in the string")
    
    
