estudiantes = [ "juan", "maria", "shayla", "xavi", "paula",]

#agrear un nuevo estudiante al final 
estudiantes.append("luis")
estudiantes.append("marcos")
estudiantes.append("edwin")
estudiantes.append("adriana")
estudiantes.append("valerie")
print(estudiantes) #['juan', 'maria', 'shayla', 'xavi', 'paula', 'luis']
 #obtener la cantidad de estudiantes
print(len(estudiantes)) #4

#buscar si un estudiante esta en la lista
if "juan" in estudiantes:
    print("juan esta en la lista") #juan esta en la lista

    #eliminar un estudiante de la lista
estudiantes.remove("juan")
print(estudiantes) #['maria', 'marcos', 'edwin', 'adriana', 'valerie', 'shayla', 'xavi', 'paula', 'luis']
