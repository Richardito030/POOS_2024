#los errores de exepciones en un lengujae de progragramacion no es otra cosa que los errores
#en tiempo de ejecucion cuando se manejan los errores mediante las excepciones en realidad
#se dice que se evita que se presentee esos errores en el programa en el tipo de ejecucion 
#se presenta un error cuando no es generada una variable
try:
             nombre=input("Escribe nombre completo de la perosna:")
             if len(nombre)>0:
                 nombre_usuario="El nombre del ususario en ele sistema es:"+nombre
             print(nombre_usuario)

except:
      print("Es necesario introducir un nombre de una persona")

#ejemplo2
try:
    nombre = input("Escribe nombre completo de la persona: ")
    numero = int(input("Escribe un número: "))  # Asumiendo que 'numero' debería ser ingresado por el usuario
    if numero > 0:
        print("soy un número positivo")
    else:
        print("soy un número negativo")
except ValueError:
    print("No es posible usar caracteres tipo letra")

#ejemplo 3
try:
    nombre = input("Escribe nombre completo de la persona: ")
    numero = int(input("Escribe un número: "))  # Asumiendo que 'numero' debería ser ingresado por el usuario
    print("cuadrado de un número: " + str(numero * numero))  # Corrigiendo el cálculo del cuadrado
except TypeError:
    print("Ocurrió un error de tipo")
except Exception as e:
    print("Ocurrió un error:", str(e))
