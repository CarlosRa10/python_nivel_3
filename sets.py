#Se declaran de dos maneras....1) set(1,2,3,4) y de esta manera 2) {1,2,3,4}
#los sets solo admiten elementos unicos,  no se repiten
#no estan ordenado en indice
#Es inmutable
#no incluye lista ni diccionario

mi_sets = set([1,2,3,4,5])
print(type(mi_sets))
print(mi_sets)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#no puedes modificar ni ver el indice
#Aceptan tuplas porque tambien son inmutables
mi_sets = set([1,2,3,4,5,1,2,(1,2,3),7,9,5,3,6,2,8,8])
print(type(mi_sets))
print(mi_sets)

#len para saber cuantos elementos hay
mi_sets = set((1,2,3,4,5))
print(type(mi_sets))
print(len(mi_sets))

#consultas
print(2 in mi_sets)

#union de sets
set1 = set((1,2,3))
set2 = {3,4,5}
set3 = set1.union(set2) #.union para unir
print(set3)
#Metodo add para agregar
set1.add(4)
print(set1)
#para eliminar
set1.remove(3)
print(set1)
#metodo para descartar
set1.discard(1)#No da erros si no esta el numero que desea eliminar
print(set1)
#metodo para eliminar
set1.pop()#como no hay indices, eliminara un elemento de manera arbitrario
print(set1)
#metodo para limpiar
set1.clear()
print(set1)

###EXAMEN###

mi_sets_1 = {1, 2, "tres", "cuatro"}
mi_sets_2 = {"tres", 4, 5}
mi_sets_3 = mi_sets_1.union(mi_sets_2)
print(mi_sets_3)


sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)


sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add('Damián')
print(sorteo)

