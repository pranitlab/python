a = int(input("enter the age : "))

#if first statement:1
if(a%2 == 0):
    print(" a is even ")
    
    print("end of if statement no.1")

#if second statement:2
#if else elif ladder
if(a>=18):
    print("above the age of concent")
    print("good for you")
    
elif(a<0):
    print("you are entering invalid input")
    
elif(a==0):
    print("entering invalid age")
    
else:
    print("below the age of concent")
    print("end of program")