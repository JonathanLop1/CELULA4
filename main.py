import time

# Función para hacer la pregunta y calcular el promedio de respuestas correctas
def hacer_pregunta():
    respuestas_correctas = 0
    respuestas_incorrectas = 0

    # Lista de preguntas y respuestas correctas
    preguntas = [
        {"pregunta": "La capital de Grecia es:", "opciones": ["A. Esparta", "B. Roma", "C. Atenas", "D. Poseidon"], "respuesta_correcta": "C"},
        # Puedes agregar más preguntas aquí en el mismo formato
    ]
    
    # Recorrer las preguntas
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        while True:
            opcion = input("Elige una opción (A, B, C o D): ")
            
            if opcion == pregunta["respuesta_correcta"]:
                print("Respuesta Correcta...")
                respuestas_correctas += 1
                time.sleep(1)
                break
            elif opcion in ["A", "B", "D"]:
                print("Respuesta Incorrecta...")
                respuestas_incorrectas += 1
                time.sleep(1)
                break
            else:
                print("Opción no válida. Intente con una opción válida (A, B, C o D).")

    # Calcular el promedio o porcentaje de respuestas correctas
    total_preguntas = len(preguntas)
    porcentaje_correctas = (respuestas_correctas / total_preguntas) * 100

    print(f"\nResumen de respuestas:")
    print(f"Respuestas correctas: {respuestas_correctas}")
    print(f"Respuestas incorrectas: {respuestas_incorrectas}")
    print(f"Porcentaje de respuestas correctas: {porcentaje_correctas}%")

# Llamar a la función
hacer_pregunta()

