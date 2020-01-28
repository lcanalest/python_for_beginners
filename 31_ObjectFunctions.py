# Object Functions (4:08:30)

from Student import  Student

student1 = Student("Pepe", "Tech", 3.9, True)
student2 = Student("Pepa", "Psychology", 3.1, False)

print(student1.name + ", " + str(student1.on_honor_roll()))
print(student2.name + ", " + str(student2.on_honor_roll()))