#metodos de string
#index() , format()
#upper() = pasar a mayúsculas
#lower() = pasar a minúsculas
#split() = separalo en partes (lista)
#join() = unir items usando separador
#find() = encontar un sub-string
#replace() = reemplazar un sub-string

texto = "Este es el texto de Carlos"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split() #elementos separados
print(resultado)

resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "_".join([a,b,c,d])
print(e)

resultado = texto.find("s")#la diferencia de index es que este si no lo consigue no te arroja error si no que te inmprime un -1
print(resultado)

resultado = texto.find("g")
print(resultado)

resultado = texto.replace("Carlos","Eduardo")
print(resultado)

resultado = texto.replace("e","o")
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

cambio = frase.replace("difícil", "fácil").replace("mala", "buena")

print(cambio)

###EXAMEN###

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
resultado = frase.upper()
print(resultado)

lista_palabras =" ".join(["La","legibilidad","cuenta."])
print(lista_palabras)

frase="Si la implementación es difícil de explicar, puede que sea una mala idea."
metodo=frase.replace("difícil","fácil").replace("mala","buena")
print(metodo)