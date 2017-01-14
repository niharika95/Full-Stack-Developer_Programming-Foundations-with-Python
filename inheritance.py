class Parent():
    def __init__(self, lastName, eyeColor):
        print("Parent Constructor called")
        self.lastName = lastName
        self.eyeColor = eyeColor

    def showInfo(self):
        print("Last Name: " + self.lastName)
        print("Eye Color: " + self.eyeColor)    
        
class Child(Parent):
    def __init__(self, lastName, eyeColor, toys):
        print("Child Constructor called")
        Parent.__init__(self, lastName, eyeColor)
        self.toys = toys

    def showInfo(self):
        print("Last Name: " + self.lastName)
        print("Eye Color: " + self.eyeColor)
        print("Toys: " + str(self.toys))

billyCyrus = Parent("Cyrus", "green")
#print(billyCyrus.lastName)
#billyCyrus.showInfo()
mileyCyrus = Child("Cyrus", "blue", 7)
mileyCyrus.showInfo()
#print(mileyCyrus.lastName)
#print(mileyCyrus.toys)


