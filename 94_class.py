class Employee:
    language = "py"    #this is an class attribute
    salary = 10
    
pranit = Employee()
pranit.name="pranit"   #this is an instance attribute
print (pranit.name,pranit.language ,pranit.salary)

pandu = Employee()
pandu.name="pandu"
print(pandu.name,pandu.salary ,pandu.language)


#here name is an instance attribute and language and salary is an class attributee