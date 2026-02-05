class Employee:
    language= "python"  #This is a class attribute
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    
    def greet(self):
        print("Good morning")    


harry= Employee()
# harry.language="javascript" #This is an instance attribute
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)
