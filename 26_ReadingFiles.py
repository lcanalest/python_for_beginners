# Reading Files (3:12:42)
## Diferentes modos
## r = read
## w = write
## r+ = read & write
## a = append

employees = open("employees.txt", "r")
print(employees.read())
employees.close()

print("")
employees = open("employees.txt", "r")
for employee in employees.readlines():
    print(employee)
employees.close()


