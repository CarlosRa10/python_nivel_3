#Concepto o plabara clave : y un valor asociado a esa clave
#diccionario = {Clave : Valor, clave2 : valor2}
#es para almacenar valores a los que puedas acceder sin conocer su ubicación exacta

diccionario = {'clave1':'valor1','clave2':'valor2'}
print(type(diccionario))
print(diccionario)

#Consultar

resultado = diccionario['clave1']
print(resultado)

cliente = {'Nombre':'Carlos','Apellido':'Ramirez','Peso':60.5,'Talla':42}
consulta = cliente['Talla']
print(type(consulta))

dic = {'clave1':55,'clave2':[10,20,30],'clave3':{'c1':10,'c2':20}}
print(dic['clave2'][1])
print(dic['clave3']['c1'])

dic2 = {'clave1':['a','b','c'],'clave2':['d','e','f']}
print(dic2['clave2'][1].upper())#Cambiar a mayuscula

#Agregar un elemento a un diccionario que ya ha sido creado

dic3 = {1:'a',2:'b'}
print(dic3)
dic3[3] = 'c'
print(dic3)

#Sobreescribir
dic3[2] = 'B'
print(dic3)

#Metodos para traer todas las claves y valores

print(dic3.keys())#Claves
print(dic3.values())#Valores
print(dic3.items())#Todos los elementos

###EXAMEN###

mi_dic = {'nombre': 'Carlos','apellido':'Ramirez','edad': 24,'ocupacion':'Estudiante'}
print(mi_dic)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic = {'nombre': 'Carlos','apellido':'Ramirez','edad': 24,'ocupacion':'Estudiante'}
mi_dic['apellido'] = 'Espinoza'
mi_dic['pais'] = 'Venezuela'
print(mi_dic)



