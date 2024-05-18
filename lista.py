mi_lista = ["a","b","c"]
otra_lista = ["hola",10,10.5]
print(type(mi_lista))

resultado = len(mi_lista)#cantidad de elementos
print(resultado)

resultado = mi_lista[0]
print(resultado)

mi_lista2 = ["d","e","f"]
resultado = mi_lista + mi_lista2
print(resultado)
#las listas pueden alterar sus elementos

mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "Alpha"
print(mi_lista3)
mi_lista3.append("g") #Agregar un elemnto a la lista original
print(mi_lista3)
mi_lista3.pop()#elimina el ultimo elemento al menos que pases el indice por parametro
print(mi_lista3)
eliminado = mi_lista3.pop(0)
print(eliminado)

lista = ["g","o","b","m","c"]
lista.sort()#Ordena
#sort realiza una accion pero no devuelve nada
print(lista)

lista.reverse()#dar vuelta el orden alfabetico
print(lista)

###EXAMEN###

lista = ["hola","mundo",10,10.10,"chao"]
print(lista)

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)