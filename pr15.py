# Object Oriented Programming

class Employee:
    name = "jaydip"
    language = "python"  # Class Attribute
    salary = 12000

jaydip = Employee()
jaydip.l = 'computer' # Instance Attribute
print(jaydip.l, jaydip.name, jaydip.language, jaydip.salary)





class oop:
    Subject = "python"
    Marks = 20

    def __init__(self, Subject, Marks) -> None:  # Dunder method which is automatically called
        self.Subject = Subject
        self.Marks = Marks
        print("hello jaydip good to see you")

    @staticmethod
    def Function():
        print("hello jaydip")

computer = oop("C", 12)
#computer.Subject = "Java"
print(computer.Marks, computer.Subject)
# Output 20 Java
computer.Function()



# Inheritance
# Single Inheritance

class A:
    def animal(self,sound, voice):
        self.sound = sound
        self.voice = voice

class B:

    def animal2(self):
        print("hello jaydip")

class C(B,A): #Multiple Inheritance

    def animal3(self):
        print('hello class c')

obj1 = C() # Multilevel Inheritance
obj1.animal3()
obj1.animal('dog', 12)
print(obj1.sound, obj1.voice)
obj1.animal2()


# Encapsulation in python

