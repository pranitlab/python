class employe:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the employe is{self.name} and th company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all labguages here is the language:{self.language}")
        
class programmer(employe,coder):
    company = "itc Infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}language")
        
        
a = employe()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()