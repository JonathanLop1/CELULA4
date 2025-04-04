# Formato en forma de diccionario para las preguntas
formato = [
    {"pregunta1":""},
    {"pregunta2":""},
    {"pregunta3":""},
    {"pregunta4":""},
    {"pregunta5":"C"}
]
print("Bienvenido a preguntas y respuestas","")


import time 

def pregunta5():
    while True:
        print("""La capital de Grecia es:
            A. Esparta 
            B. Roma
            C.Atenas
            D.Poseidon""")
        print("A. ")
        print("B. ")
        print("C. ")
        print("D. ")
        
        opcion = input("Elige una opcion (A,B,C o D): ")
        
        if opcion == "A":
            print("Respuesta incorrecta...")
            time.sleep(1)
            
        elif opcion == "B":
            print("Respuesta incorrecta...")             
            time.sleep(1)
             
        elif opcion == "C":
            print("Respuesta Correcta...")
            time.sleep(1)
        
        elif opcion == "D":
            print("Respuesta incorrecta...")             
            time.sleep(1)    
            break
        else:
            print("Opcion no valida. Intente con una opcion valida (A,B,C o D).")
        break
pregunta5()