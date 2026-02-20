class Student:
    school="KBTU"

    def __init__(self, name):
        self.name=name

s1=Student("Tomiris")
s2=Student("Madina")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)