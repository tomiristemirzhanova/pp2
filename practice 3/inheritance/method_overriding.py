class Animal:
    def speak(self):
        print("it makes a sound")

class Cat(Animal):
    def speak(self):
        print("Cat sys meow")

a=Animal()
c=Cat()

a.speak()
c.speak()


#it makes a sound
#cat says meow