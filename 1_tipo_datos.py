# -*- coding: latin-1 -*-

""" 
TIPO DE DATOS EN PYTHO

Enteros:  en este grupo están todos los números, enteros y long:
    ejemplo: 1, 2.3, 2121, 2192, -123

Booleanos (bool): Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ):
    ejemplo: True, False

Cadenas (str): Son una cadena de texto :
    ejemplos: ?Hola?, ?�C�mo estas??

Listas: Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:
    ejemplos: [1,2,3, ?hola? , [1,2,3] ], [1,?Hola?,True ]

Diccionarios: Son un grupo de datos que se acceden a partir de una clave:
    ejemplo: {?clave?:?valor?}, {?nombre?:?Fernando?}

Tuplas: tambi�n son un grupo de datos igual que una lista con la diferencia que una tupla despu�s de creada no se puede modificar.
    ejemplos: (1,2,3, ?hola? , (1,2,3) ), (1,?Hola?,True) (Pero jam�s podremos cambiar los elementos dentro de esa Tupla)

En Python trabajas con módulos y ficheros que usas para importar las librer�as.


Funciones:
Las funciones las defines con def junto a un nombre y unos paréntesis que reciben los parámetros a usar. Terminas con dos puntos.
def nombre_de_la_funci�n(parametros):
Después por indentación colocas los datos que se ejecutar�n desde la funci�n


 """

# Suma
suma = 2 + 2
print(suma )
print('hola texto printt')



# Variables: a diferencia de los demás lp, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. 
A = 8 
B = A
print(B)

#Listas: Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.
L = [22, True, 'una lista', [1, 2]] 
L[0] # 22

#Tuplas: Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.
T = (22, True, "una tupla", (1, 2)) 
T[1]  # True

#Diccionarios: En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, 
# el segundo dato será el dato al cual accederás con la llave. 
# Recuerda que los diccionarios son listas de llave:valor.
D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"} 
D["Kill Bill"]  # "Tamarino"


#Conversiones

#De flotante a entero:
int (4.3)   #4

#De entero a flotante:
float(4)    #4.0

#De entero a string:
str(4.3)    #"4.3"

#De tupla a lista:
list((4, 5, 2))  #[4, 5, 2]


#Operadores Comunes
#Longitud de una cadena, lista, tupla, etc.:

len("key") 
    #3

#Tipo de dato:
type(4) #4



#Condicionales IF
if ( 9 > 5 ):
 	print('mayor') 
elif ( a == b ): 
 	print('menor')  
else:
 	print('igual') 


#Bucle FOR

#for i in ____:
# 	elementos

#Bucle WHILE
#while (condición):
# 	elementos



#Operadores Básicos

2+2
#4
5-2
#3
3*4
#12
5/4
#1
5.0/4.0
#1.25
9 % 2
#1
10 % 2
#0
3**2
#9
3 > 5
#False
5 < 10
#True
10 == 10
#True
10 == 9
#False
