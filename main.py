# Formato en forma de diccionario para las preguntas
# formato = [
#     {"pregunta1":""},
#     {"pregunta2":""},
#     {"pregunta3":""},
#     {"pregunta4":""},
#     {"pregunta5":""}
# ]
# print("Bienvenido a preguntas y respuestas","")


# 

puntaje = 0
num_preguntas = 3

respuesta = input(f'Serán {num_preguntas} preguntas ¿Preparado para jugar? (si/no) :')

if respuesta.lower() == 'si':
    respuesta = input('Pregunta 1: ¿Cual es la capital de Hungria?')
    if respuesta.lower() == 'budapest':
        puntaje += 1
        print('¡Correcto! :D')
    else:
        print('Incorrecto :(, la respuesta es: Budapest')
 
 
    respuesta = input('Pregunta 2: ¿Cual es la capital de Chile?')
    if respuesta.lower() == 'santiago':
        puntaje += 1
        print('¡Correcto! :D')
    else:
        print('Incorrecto :(, la respuesta es: Santiago')
 
    respuesta = input('Pregunta 3: ¿Cual es la capital de Ecuador?')
    if respuesta.lower() == 'quito':
        puntaje += 1
        print('correct')
    else:
        print('Incorrecto :(, la respuesta es: Quito')

        
    
