# Writting to files (3:21:25)

## Adicionar un registro al final
employees_file = open("employees.txt", "a")
employees_file.write("\nCoco - Human Resources")
employees_file.close()

## Sobreescribir un archivo
employees_file = open("employees.txt", "w")
employees_file.write("Coco - Human Resources\nSabuesito - Chipi\nTusan - Chiquillo\n")
employees_file.close()

## Crear un archivo
employees_file = open("employees2.txt", "w")
employees_file.write("Coco - Human Resources\nSabuesito - Chipi\nTusan - Chiquillo\n")
employees_file.close()