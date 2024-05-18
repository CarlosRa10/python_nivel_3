#los string de python tiene mas de 30 métodos que nos permite manipularlo y analizarlo...
#la clase de hoy sera de index() o indice
#un string es una secuencia de caracteres
#"HOLA" H = 0, O = 1, L = 2, A = 3.... siempre el indice empieza con 0
#index() sirve para dos cosas
#1- conocer el índice de un caracter
#2-conocer qué caracter hay en un índice

mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[-4]
print(resultado)
#com indices negativos se empieza con 0 a la izquierda y luego -1 a la derecha
resultado = mi_texto.index("n")#si buscamos una letra que no tenemos dara error
print(resultado)
resultado = mi_texto.index("prueba")#tiene que ser exacto
print(resultado)
resultado = mi_texto.index("a")#Si una letra se repite solo dara el resultado de la primera que consiguio y luego de detiene
print(resultado)
resultado = mi_texto.index("a",5)#a partir de que indice buscar la letra
print(resultado)
resultado = mi_texto.index("a",5,11)#el numero "11" del ultimo parametro no es inclusivo, hay que agregarle un numero mas "12"
print(resultado)
resultado = mi_texto.rindex("a")#busca al revez... de derecha a izquierda
print(resultado)

###EXAMEN###
palabra = "ordenador"
resultado = palabra[4]
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)

