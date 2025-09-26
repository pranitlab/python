a = int(input("enter the number"))
b = int (input("enter ths second number"))

if (b==0):
    raise ZeroDivisionError("hey our program is not meant to be divide number by zero")
else:
    print(f"the division a/b is {a/b}")
