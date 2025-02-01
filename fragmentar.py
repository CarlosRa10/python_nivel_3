#Otra forma distinta de manipular string
#extraer porciones de texto
#slicing = rebanar o cortar en rodajas en ingles
#mi_variable[5:12:2] el primer argumentoindica desde donde,
# el segundo indica hasta donde pero sin contar el ultimo numero
#y el tercer argumento indica cada cuanto caracteres se va a selecionar nuestro fragmento
#inicio:fin:paso
#mi_texto = [inicio_busqueda :  limite_busqueda - 1 :  saltos]
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::3]
print(fragmento)
fragmento = texto[::-1]
print(fragmento)
palabra = 'Este es un texto de prueba'
print(palabra[10:5:-1])

###EXAMEN###

frase = "Controlar la complejidad es la esencia de la programación"
fragmentar = frase[0:9]
print(fragmentar)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmentar = frase[8::3]
print(fragmentar)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmentar = frase[::-1]
print(fragmentar)
