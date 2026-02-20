class Mom:
    def cook(self):
        print("Mom can cook")

class Dad:
    def drive(self):
        print("Dad can drive")

class Child(Mom, Dad):
    pass

c=Child()

c.cook()
c.drive()


#mom can cook
#dad can drive