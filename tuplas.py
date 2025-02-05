#Las tuplas es una colección de elementos inmutables
#ocupan menos espacio en memoria a comparación de una lista (eficiencia)
#Sirven para crear esctucturas que no se van a modificar es decir, son apruebas de daños
mi_tuple = (1,2,3,4) #Se pueden poner incluso sin parentesis ()
print(type(mi_tuple))
print(mi_tuple)
#Anidar
t = (5,5.5,'hola',['a','b','c'],{'nombre':'Carlos'},(1.2))
print(t[3][1])
#Casting
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
#asignar contenido
t = (1,2,3)
x,y,z = t
print(x,y,z)

t = (1,2,3,1)
#x,y,z = t
print(len(t))#te dice cuantos elementos hay no indices
print(t.count(1))#count te permite contar las apariciones de un valor
print(t.index(2))#Consulta en que indice se encuentra

###EXAMEN###
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tuple)
print(type(mi_lista))

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tuple
print(a, b, c, d)