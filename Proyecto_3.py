#programar un analizador de texto
#pedir al usuario que ingrese un texto-listo
#luego que ingrese 3 letras a su eleccion-listo
#El programa realizara 5 tipos de analisis
#cuantas veces aparece cada una de las letras/almacena las letras en una lista/pasar textos y letras a minusculas- listo
#cuantas palabras hay en total/metodo de string - listo
#primera y ultima letra/identacion-listo
#mostrar como quedaria el texto si lo invertimos-listo
#aparece python /usar bool y diccionario

texto = str(input("Ingresa un texto: "))
letras = []
texto = texto.lower()

letras.append(input("Ingrese la primera letra: ".lower()))
letras.append(input("Ingrese la segunda letra: ".lower()))
letras.append(input("Ingrese la tercera letra: ".lower()))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)}")

print("\n")
print("LETRAS DE INICIO Y FIN")

letra_inicio = texto[0]
letra_fin = texto[-1]

print(f"La letra inicial es '{letra_inicio}' y letra final es '{letra_fin}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")


'''texto = input("Ingrese un texto: ").lower()
print(texto)
letras = []
letras.append(input('Ingrese la primera letra: ').lower())
letras.append(input('Ingrese la segunda letra: ').lower())
letras.append(input('Ingrese la tercera letra: ').lower())
print(letras)

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_fin}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
invertido = " ".join(palabras)
print(f"Tu texto invertido es:\n'{invertido}'")

print("\n")
print("BUSCANDO LA PALABRA 'PYTHON' ")
buscar_python = "python" in texto
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")


'''