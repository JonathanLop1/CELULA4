def bienvenida():
    
    print("=" * 60)
    print("🌟 BIENVENIDO AL CUESTIONARIO DE CONOCIMIENTOS GENERALES 🌟")
    print("=" * 60)
    print()
    print("👋 ¡Hola! Prepárate para responder algunas preguntas divertidas.")
    print("📋 Solo necesitas escribir la letra de la opción que creas correcta.")
    print("✅ Por cada respuesta correcta ganarás un punto.")
    print("❌ Por cada incorrecta, no te preocupes, ¡seguirás aprendiendo!")
    print()
bienvenida()


def preguntas():
    formato = [
        {"pregunta1":"C"},
        {"pregunta2":""},
        {"pregunta3":""},
        {"pregunta4":""},
        {"pregunta5":""}
    ]
    print("Bienvenido a preguntas y respuestas","\n")
    while True: 
        print("Primera pregunta","\n")
        print("¿Cual es la capital de Francia?","\n")
        opcion_a_1 = input("A. Berlin")
        opcion_a_2 = input("B. Madrid")
        opcion_a_3 = input("C. Paris")
        opcion_a_4 = input("D. Roma")
preguntas()
    