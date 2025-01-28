# #      0 1  2  3 4 5          
lista=[1,76,65,9, "lol",7,54]
# # #      -6 -5-4 -3-2-1

# # # print(lista)

# # # lista.append(3,"Mario")

# # # print(lista)

# # # # for i in lista:
# # #     print("Elemento ",i)

# # # while True:
    
# # #     print(lista)
# # #     m=int(input("Agregue u nuevo elemento"))
# # #     lista.append(m)
# # #     print(lista)
    
# # print(lista)

# # lista.insert(3,round(856.897))

# # print(lista)


# # print(lista)

# # lista.remove(76)

# # print(lista)

#  #      0           1      2
# lnom=["Pedro", "Juan", "Diego"]
# # ape=["Pascal", "Santaolaya", "Robles"]
# # car=["primer", "segundo", "tercer"]

# # for i in range(len(lnom)):
# #     print(" El", car[i], " nombre es ", lnom[i],ape[i])
    

# # print(lista)

# # lista.reverse()

# # print(lista)


# print(lnom)

# lnom.sort()

# print(lnom)

###prototipo de boleta con listas



# lnom=["Pedro", "Juan", "Diego"]
# frutas=["uva", "melon", "melame", "pera", "fresa", "platano"]
# pfru=[1300,1000,1500, 900, 1800, 1400]
# c=1
# car=[]
# total=0

# print("Quien va a comprar?")
# for i in lnom:
#     print(c,'.-',i)
#     c+=1
# sel=int(input())-1

# # print(lnom[sel])

# print("Bienvenido ",lnom[sel], "al la Fruteria" )

# while len(car)<3:
#     for fruta in range(len(frutas)):
#         print(fruta+1, ".-", frutas[fruta])
#     selfru=int(input("Selecciones una fruta"))-1
#     print("Usted ha seleccionado ", frutas[selfru], "y su precio es", pfru[selfru] )
#     car.append(selfru)
#     print(car)
# print("Verdureria Pelayos")
# for i in car:
#     print(f"",frutas[i],"......",  pfru[i])
#     total=total+ pfru[i]

# print("Su total fue ", total, "vuelva pronto ",lnom[sel])    

   
    
    
# num=8
# pares=[]
# impares=[]

# for i in range(num):

#     if  (i+1)%2==0:
#         pares.append(i+1)
#     else:
#         impares.append(i+1)
# print("Pares= " , pares)
# print("Impares= " , impares)

# lista.append(3) #agrega una elemento al final de la lista
# lista.insert(2, 4) #agrega un elemento en el indice indicado en el primer argumento 
# lista.remove(3) #remueve o elimina el elemento ingresado en el argumento
# lista.count() #mustra el total de elementos
# lista.clear() #elimina todos los elementos de la lista
# lista.sort() #ordena la lista de forma ascendente
# lista.reverse() # ordena la lista de forma inversa
# lista.index(4) #muesta el indice del elemento que va enn el argumento


# marcas=[]
# korn=""
# while korn!="0":
#     korn=input("Ingrese una marca")
#     marcas.append(korn)
# marcas.sort()
# print(marcas)

#temp=[29, 28, 34, 30, 33, 29,35,29, 28, 34, 30, 33, 29,35, 20,20]

# print(round(sum(temp)/len(temp)))

# print(temp)

# for i in temp:
#     if i>=30:
#         print(i,"Hace mucho calor")
#     else:
#         print(i,"Hce calor ")
        
# import random

# # print(num)
# loteria=[]

# for h in range(7):
#     num=random.randint(1,38)
#     loteria.append(num)
#     loteria.sort()
# print(loteria)

# colo=[]
# u=[]
# opc="1"
# while opc!="0":
#     print("A que euipo desea agregar ? Para salir presione cero(0)")
#     opc=input()
#     if opc=="u"and opc!=0:
#         nj=int(input("ingrese el numero del jugador"))
#         u.append(nj)
#     elif opc=="colo"and opc!=0:
#         nj=int(input("ingrese el numero del jugador"))
#         colo.append(nj)   
#     print(u)
#     print(colo)    


#matriz una lista compuesta por listas

   # 0 1     0 1 2
# matriz= [[[2,7,5],   #0
#          [3,4,7],    #1
#          [9,1,2]],   #2
#          [[21,32,65],#  0 lista dos
#           [54,61,28],#1 lista dos
#          [15,20,26]]#2 lista dos
#          ]

# print(matriz[1][2][2])

# for i in matriz:
#     print(i)


# d={"nombre:""link huispe"}
# producto= {
#     "uva":1400,
#     "pera":1200,
#     "melon":1000,
#     "verduras":{"papa":600, "tomate":800,"cebolla":500}
# }

# print(producto)

# for clave,valor in producto.items():
#     print(f"{clave}= ${valor}")

# nombres=["yessica", "mario", "pedro"]

# for i in range(3):
#     nombres.append(nombres)
#     print(nombres)

#nombre_mlargo=max(nombres,key=len)
#print(f"El nombre mas largo es: {nombre_mlargo}") 

# nombres =["yessica","ronald","monica"]
# for i in range(3):
#     nombres=input("Ingrese un nombre: ")
#     nombres.append(nombres)
    


# apellidos=["silva","muños","rubilar"]

# for i in range(3):
#     apellidos=input("ingrese un apellido: ")
#     apellidos.append(apellidos)
#     

# nombres.sort()
# apellidos.sort()

# print("nombres ordenados: ",nombres)


nombres = []
apellidos = []

for i in range(3):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

for i in range(3):
    apellido = input("Ingresa un apellido: ")
    apellidos.append(apellido)

nombres.sort()
apellidos.sort()

print("Nombres ordenados:")
for nombre in nombres:
    print(nombre)

print("Apellidos ordenados:")
for apellido in apellidos:
    print(apellido)



