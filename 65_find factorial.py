# 5! = 1X2x3x4x5


n = int(input("enter the number"))

product = 1
for i in range(1,n+1):
    product = product*i
    
print(f"the factorial of given number {n} is {product}")
    