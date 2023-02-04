# dog3.py, Chapter 9, Python Crash Course
# program executes a dog class

class Dog():
    """a simple attempt to model a dog"""
    def __init__(self, name, age):
        self.name = name    # attribute
        self.age = age      # attribute


    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()



