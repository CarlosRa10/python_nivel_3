#programar un analizador de texto
#pedir al usuario que ingrese un texto-listo
#luego que ingrese 3 letras a su eleccion-listo
#El programa realizara 5 tipos de analisis
#cuantas veces aparece cada una de las letras/almacena las letras en una lista/pasar textos y letras a minusculas- listo
#cuantas palabras hay en total/metodo de string - listo
#primera y ultima letra/identacion-listo
#mostrar como quedaria el texto si lo invertimos-listo
#aparece python /usar bool y diccionario


texto = str(input("Ingresa un Texto: "))
texto = texto.lower()
letras = []
letras.append(str(input("Ingresa la primera letra a analizar: ".lower())))
letras.append(str(input("Ingresa la segunda letra a analizar: ".lower())))
letras.append(str(input("Ingresa la tercera letra a analizar: ".lower())))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_de_letras1 = texto.count((letras[0]))
cantidad_de_letras2 = texto.count((letras[1]))
cantidad_de_letras3 = texto.count((letras[2]))
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_de_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_de_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_de_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras")

print("\n")
print("LETRA DE INICIO Y FINAL")
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es '{primera_letra}' y la ultima letra del texto es '{ultima_letra}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"si",False:"no"}
print(f"La palabra python {dic[buscar_python]} se encuentra en el texto")


'''ingreso_texto_usuario = list(input('Ingrese un texto: ').lower())
print(ingreso_texto_usuario)
lista_letras = list(input('Eliga tres letra: ').lower())
list(lista_letras)
print(type(lista_letras))
print(lista_letras)
print(f"La letra {lista_letras[0]} se repite {ingreso_texto_usuario.count(lista_letras[0])} veces ")
print(f"La letra {lista_letras[1]} se repite {ingreso_texto_usuario.count(lista_letras[1])} veces ")
print(f"La letra {lista_letras[2]} se repite {ingreso_texto_usuario.count(lista_letras[2])} veces ")
list(ingreso_texto_usuario)
print(ingreso_texto_usuario)
print(f"El texto introducido por el usuario tiene {len(ingreso_texto_usuario)} letras")
print(f"La primera letra del texto es {ingreso_texto_usuario[0]}")
print(f"La ultima letra del texto es {ingreso_texto_usuario[-1]}")
normal ="".join(ingreso_texto_usuario[:])
#print(normal)
revez = "".join(ingreso_texto_usuario[::-1])
print(f"El texto invertido se ve asi:\n{revez}")
piton = "python" in normal
dic = {True:"si",False:"no"}
print(piton)
print(f"La palabra 'Python' {dic[piton]} se ncuenta en el texto")'''