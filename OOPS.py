'''class Employee:
    language="Python"
    salary=120000
    def __init__(self, name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getinfo(self):
        print(f"the language is{self.language}.The salary is{self.salary}")

    @staticmethod
    def greet(): 
        print("good morning")

harry=Employee("Harry",130000,"js")
print(harry.name,harry.salary,harry.language) 
'''
class programmer:
    company='microsoft'
    def __init__(self,name,pin,salary):
        self.name=name
        self.pin=pin
        self.salary=salary
p=programmer("prasad",581301,120000)
print(p.name,p.salary,p.pin,p.company)
