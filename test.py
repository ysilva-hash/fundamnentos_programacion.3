# nombre="yessica silva"
# edad= 26
# print("Mi nombre es ",nombre, "mi edad es ",edad)



# print("ingrese un numero")
# num1=int(input())

# print("ingrese otro numero")
# num2=int(input())
# print(num1 + num2)

# print("ingrese un numero")
# num1=int(input())
# if num1>18:
#     print("ustes es mayor de edad")
    
# else:
#     print("usted es un bebe")  

num1=0
num2=0
num3=0

# print("ingresa un numero")
# num1=int(input()) 

# print("ingresa el segundo numero")
# num2=int(input())

# print("ingrese el tercero")
# num3=int(input())
# print((num1+num2+num3)/3) 

# parque nacional que tiene los siguentes valores

# menor de 12 $500
# entre 13 y 18 $1000
# entre 19 y 64 $2000
# mas de 65 $700

print("bienbenido ¿que edad tiene usted?")

edad=int(input())
print("ingrese su edad: ")

if edad <12:
    monto=500
    print("su entrada cuesta $500")

elif edad>=13 and edad <=18:
    monto=1000
    print("el valor de su entrada es de $1000")

elif edad>=19 and edad< 64:
    monto=2000
    print("el valor de su entrada es de $2000")

elif edad>=65:
    monto=700
    print("el valor de su entrada es de $700")
    
else:
    print("Error")                
    
entradas=0

print("cuantas entrads quiere?")

cantidad=int(input())
total=cantidad*monto

print('su total es ', total)     

print("bienvenido") 
print("usted pertenece a la florida?")

opcion1= 'si'
opcion2= 'no'

if opcion1=="si":
    print("continua a la siguente")
else:
    print("vuelva a intentarlo") 
print("Tiene carnet de socio?")
if opcion1=="si":
   print("ingrese su numero")
else:
    print("vuelva a intentarlo")

print("es juvilado?")
if opcion1=="si":
    print(f"paga monto con descuento {25%} ")
else:
    print("vuelva a intentarlo")  

if opcion2=="no":
    print("gracias por su visita")
       
      