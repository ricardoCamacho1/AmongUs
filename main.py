import random
rol = ["Impostor", "Tripulante"]
opcion = random.choice(rol)

# Variables globales

volver_a_jugar = ""
contador = 0
gomita = 0
acabar = 0
final = 0
puntos_finales = 0

# Listas globales

jugadores = []
sopa_de_letras = []
palabras = []

# Lista de Letras

letras = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

# Nombre del Jugador

nombre = str(input("¿Quieres Jugar Among Us?\nIngresa tu nombre:\n\n"))

#Leer Archivo de Jugadores

nombres = open("jugadores.txt", "r")
while True:
    nombres_readed = nombres.readline()
    if len(nombres_readed) == 0:
        break
    nombres_readed = nombres_readed.replace("\n", "")
    jugadores.append(nombres_readed)
jugadores.append(nombre)  
nombres.close()

#Listas de Preguntas

opcion_multiple = [
    [
        "\n¿Qué significa ADN?",
        [
            "\n1) Ácido Ribonucléico", "2) Ácido Desoxirribonuléico",
            "3) Ácido Desoxirribonucléico\n"
        ], "3"
    ],
    [
        "\n¿Cuál es el nombre del elemento K de la tabla periódica? (Se encuentra en el plátano)",
        ["\n1) Sodio", "2) Potasio", "3) Carbono\n"], "2"
    ],
    [
        "\n¿Cuál es la velocidad de la luz?",
        ["\n1) 300,000 km/s", "2) 300,000 m/s", "3) 30,000 km/s\n"], "1"
    ],
    [
        "\n¿Cómo se llaman las partículas con carga eléctrica negativa?",
        ["\n1) Electrones", "2) Protones", "3) Neutrones\n"], "1"
    ],
    [
        "\n¿Cuál es la clasificación más importante de las células?",
        [
            "\n1) Animales y Vegetales", "2) Procariotas y Eucariotas",
            "3) Simples y Complejas\n"
        ], "2"
    ],
    [
        "\n¿Cuál es la principal función de los globulos rojos?",
        [
            "\n1)Combatir enfermedades", "2) Coagular sangre",
            "3)Llevar oxígeno\n"
        ], "3"
    ],
    [
        "\n¿Qué tipo de radiación te produce quemaduras?",
        ["\n1)Ultravioleta", "2)Rayos X", "3)Infrarroja\n"], "1"
    ],
    [
        "\nEl teorema que dice que 'en todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos' es el:",
        [
            "\n1)Teorema de Arquímedes", "2)Teorema de Pitágoras",
            "3)Teorema de Tales\n"
        ], "2"
    ],
    [
        "\n¿Qué inventó Alfred Nobel, el que da nombre a los famosos premios?",
        ["\n1)La dinamita", "2)La penicilina", "3)La bomba atómica\n"], "1"
    ],
    [
        "\nLa  columna más a la derecha de la tabla periódica esta compuesta por:",
        ["\n1)Haluros", "2)Gases nobles", "3)Minerales\n"], "2"
    ]
]

abiertas = [
    [
        "\nResuelve lo siguiente por jerarquía de operaciones e ingresa la respuesta correcta:\n8/4*2(2+2)\n",
        "16"
    ],
    [
        "\nEncuentra el valor de x e ingresa el resultado obtenido si:\n8x-4x+5=205",
        "50"
    ],
    [
        "\nResuelve lo siguiente por jerarquía de operaciones e ingresa la respuesta correcta:\n8/4*2(2+2)\n",
        "16"
    ],
    [
        "\nDadas las siguientes dos ecuaciones encuentra el valor de x y y, ingresánolo como coordenada, primero un paréntesis seguido del valor de x con una coma, seguido, sin dejar espacio el valor de y y al final un paréntesis:\nx+y =5\n2x+3y=8\n",
        "(7,-2)"
    ],
    [
        "\nDame la hipotenusa de un triángulo rectángulo cuyos catetos miden 15 y 20 cm usando el Teorema de Pitágoras\n",
        "25"
    ],
    [
        "\nEncuentra el número que cumple la condición de que la suma de su doble y su triple sea igual a 100.\n",
        "20"
    ],
    [
        "\nEn un torneo de tenis, el jugador que pierde se vuelve a casa. Cuántos jugadores iniciaron este torneo si desde la ronda preliminar hasta la final se han jugado 128 partidos.\n",
        "129"
    ],
    [
        "\nTengo 20 metros de cinta roja para hacer lazos en unos paquetes de regalo idénticos. Para cada lazo necesito 50 centímetros de cinta. ¿Cuántos lazos puedo hacer?\n",
        "40"
    ],
    [
        "\n¿Cuánto habrá que rebajar un producto para que valga lo mismo que valía antes de que incrementase un 25% su precio?(Anotalo con el signo de porcentaje)\n",
        "20%"
    ],
    [
        "\nEl monstruo del lago Ness mide 80 metros más la mitad de lo que mide, ¿cuánto mide el monstruo del lago Ness?\n",
        "160"
    ]
]

# Funciones de preguntas opción múltiple

def preguntar_op_t():
    global gomita
    global puntos_finales
    global opcion_multiple
    global jugadores
    pregunta = random.choice(opcion_multiple)
    print(pregunta[0])
    for i in range(len(pregunta[1])):
        print(pregunta[1][i], end="\n")
    respuesta = str(input())
    if respuesta == pregunta[2]:
        print(
            "\n¡Excelente! Contestaste correctamente. Sigue así para encontrar al impostor.\n ¡Salvarás la nave!\nTodavía siguen vivos ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nHas fallado, ya eliminaron a uno de tus compañeros y no has obtenido ninguna pista para saber quién es el impostor. ¡Concéntrate más!\nTodavía siguen vivos ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def preguntar_op_i():
    global gomita
    global puntos_finales
    global opcion_multiple
    global jugadores
    pregunta = random.choice(opcion_multiple)
    print(pregunta[0])
    for i in range(len(pregunta[1])):
        print(pregunta[1][i], end="\n")
    respuesta = str(input())
    if respuesta == pregunta[2]:
        print(
            "\n¡Excelente! Contestaste correctamente y has saboteado la nave. Sigue así para lograr elminar a todos los tripulantes.\nYa elminaste a uno de ellos y nadie sospecha de ti todavía.\n ¡¡Elimina a Todos!!\nTodavía siguen vivos ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nHas fallado. Ya eliminaste a uno de los tripulantes pero estuvieron apunto de verte.\nTen más cuidado y contesta correctamente las preguntas. ¡Concéntrate más!\nTodavía siguen vivos ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

# Funciones de preguntas abiertas

def preguntar_abiertas_t():
    global gomita
    global puntos_finales
    global jugadores
    global abiertas
    pregunta = random.choice(abiertas)
    print(pregunta[0])
    respuesta = input()
    if str(respuesta) == pregunta[1]:
        print(
            "\n¡Excelente! Contestaste correctamente. Sigue así para encontrar al impostor.\n ¡Salvarás la nave!\nTodavía siguen vivos ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nHas fallado, ya eliminaron a "+jugadores[0]+" y no te has acercado en saber quién es el impostor. ¡Concéntrate más!\nTodavía siguen vivos ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def preguntar_abiertas_i():
    global gomita
    global puntos_finales
    global jugadores
    global abiertas
    pregunta = random.choice(abiertas)
    print(pregunta[0])
    respuesta = input()
    if str(respuesta) == pregunta[1]:
        print(
            "\n¡Excelente! Contestaste correctamente y has saboteado la nave. Sigue así para lograr elminar a todos los tripulantes.\nYa elminaste a "+jugadores[0]+" nadie sospecha de ti todavía.\n ¡¡Elimina a Todos!!\nTodavía siguen vivos ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nHas fallado, ya eliminaste a "+jugadores[0]+" pero estuvieron apunto de verte.\nTen más cuidado y contesta correctamente las preguntas. ¡Concéntrate más!\nTodavía siguen vivos ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

# Funciones de ahorcado

def ahorcado_1_i():
    global gomita
    global jugadores
    global puntos_finales
    input(
        "\nTe tenemos un nuevo reto, esta vez con un juego llamado ahorcado.\n¿Lo conoces, no?\nTendrás que resolverlo y sólo tendrás 6 vidas. Para que no sea injusto te daremos una pequeña pista que sabemos que te ayudará para poder completar este reto:\nLa palabra que estamos buscando es un antibiótico descubierto por Alexander Fleming.\n¿Estás Listo?\nPresiona ENTER para empezar\n"
    )
    palabra = "penicilina"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\n¡Felicidades! :)\n¡Qué buena estrategia usaste haciendo fallar la electricidad!\n¡Lograste eliminar a "+jugadores[0]+" y nadie vio nada!\nCada vez fatan menos. Sigue así.\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nNo mataste a nadie y ya empezaron a sospechar de ti por estar siguiendo a alguien. Afortunadamente, tus mentiras los convencieron y sacaron a "+jugadores[0]+". Ten mucho más cuidado y no falles más que puede que en algún momento te expulsen. Échale más ganas.\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def ahorcado_1_t():
    global gomita
    global puntos_finales
    global jugadores
    input(
        "\nTe tenemos un nuevo reto, esta vez con un juego llamado ahorcado.\n¿Lo conoces, no?\nTendras que resolverlo y sólo tendrás 6 vidas. Para que no sea injusto te daremos una pequeña pista que sabemos te ayudará para poder completar este reto:\nLa palabra que estamos buscando es un antibiótico descubierto por Alexander Fleming.\n¿Estás Listo?\nPresiona ENTER para empezar\n"
    )
    palabra = "penicilina"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\nFelicidades!! :)\nSigue así y al paso que vas muy pronto descubrirás quién es el impostor y podrás salvar la nave. No te rindas, lo vas a lograr.\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nNo te rindas y sigue realizando estas tareas. Trata de hacerlas lo mejor, así el impostor no tendrá nada más que sabotear y podrán expulsarlo.\nConcéntrate más ya que acaban de matar a "+jugadores[0]+" y no viste a nadie cerca.\nTodavía quedán ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def ahorcado2_t():
    global gomita
    global jugadores
    global puntos_finales
    input(
        "\nOtra vez volveremos a jugar ahorcado.\nYa te sabes las reglas así que comencemos.\nLa palabra que estamos buscando es un proceso térmico realizado en líquidos para reducir la presencia de agentes patógenos.\n¿Estás Listo?(recuerda poner acentos)\nPresiona ENTER para empezar\n"
    )
    palabra = "pasteurización"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\n¡Felicidades! :)\nCada vez te acercas más a descubrir quién es el impostor.¡Sigue así!\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nTienes que poner más atención. Cada vez están eliminando más y más tripulantes y eliminaron a "+jugadores[0]+".\nTal vez a la próxima no correrás con la misma suerte y tú serás el eliminado.\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def ahorcado2_i():
    global gomita
    global jugadores
    global puntos_finales
    input(
        "\nOtra vez volveremos a jugar ahorcado.\nYa te sabes las reglas así que comencemos.\nLa palabra que estamos buscando es un proceso térmico realizado en líquidos para reducir la presencia de agentes patógenos.\n¿Estás Listo?(recuerda poner acentos)\nPresiona ENTER para empezar\n"
    )
    palabra = "pasteurización"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\n¡Felicidades! :)\nCada vez estás eliminando a más y más tripulantes. Al paso que vas vas a sabotear la nave y eliminarlos a todos, pero no te confíes. Eliminaste a "+jugadores[0]+". ¡Sigue así!\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nTienes que poner más atención. "+jugadores[0]+" te vió entrar a una rejilla, menos mal que termniaron por expulsarlo a él de la nave. Tal vez a la próxima no corras con la misma suerte.\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def ahorcado3_t():
    global gomita
    global jugadores
    global puntos_finales
    input(
        "\nAhorcado de nuevo.\nya no necesitas explicación ¿cierto?.\nLa palabra que estamos buscando es un poliedro de seis caras, en el que todas las caras son paralelogramos, paralelas e iguales dos a dos. Tiene 12 aristas, que son iguales y paralelas en grupos de cuatro, y 8 vértices.\n¿Estás Listo?(recuerda poner acentos)\nPresiona ENTER para empezar.\n"
    )
    palabra = "paralelepípedo"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\n¡Felicidades! :)\nLa última junta está por empezar. Creo ya estan seguros de quién es el impostor pero puede que se equivoquen, espera a la votación y verás como te fue. ¡Nada es seguro!\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nTienes que poner más atención. Eliminaron a "+jugadores[0]+" y siguen dudando acerca de quién puede ser el impostor.\nEspera que las deciciones que se tomen en la junta sean las correctas, recuerda que nada es seguro..\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def ahorcado3_i():
    global gomita
    global jugadores
    global puntos_finales
    input(
        "\nAhorcado de nuevo.\nYa no necesitas explicación ¿cierto?.\nLa palabra que estamos buscando es un poliedro de seis caras, en el que todas las caras son paralelogramos, paralelas e iguales dos a dos. Tiene 12 aristas, que son iguales y paralelas en grupos de cuatro, y 8 vértices.\n¿Estás Listo?(recuerda poner acentos)\nPresiona ENTER para empezar.\n"
    )
    palabra = "paralelepípedo"
    palabra_clave = []
    for i in range(len(palabra)):
        palabra_clave.append("_")
    print(palabra_clave)
    vidas = 6
    while "_" in palabra_clave and vidas > 0:
        print("Escribe una letra y completa la palabra:\n")
        letra = input()
        e = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_clave[i] = letra
                e = True
        if not e:
            vidas -= 1
        print(palabra_clave)
        print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
        print(
            "\n¡Lograste completar el reto!\n¡Felicidades! :)\nYa estás a nada del final, solo falta la última junta para ver a quien sacan. Estas logrando convencer de que expulsen a "+jugadores[0]+" que no es un impostor pero nada es seguro todavía. ¡Mucha Suerte!\nTodavía quedan ellos:\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "\nNo lo lograste. :(\nYa se acerca el final del juego. Una última junta está por comenzar y están sospechando de ti. Esperemos que te crean y a ver si los connvences de expulsar a "+jugadores[0]+"\nTodavía quedan ellos:\n"
        )
        del jugadores[-1]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

# Funciones de Sopa de Letras

def sopa_t():
    global gomita
    global jugadores
    global puntos_finales
    global letras
    global sopa_de_letras
    global palabras
    tamanio_sopa_de_letras = 30

    palabras_archivo = open("PalabrasSopaDeLetras.txt", "r")

    for palabra in palabras_archivo:
        palabra_string = palabra.replace("\n", "")
        palabra_list = palabra_string.split(";")
        palabras.append(palabra_list)

    def llenar_matriz_sopa_de_letras():
        for i in range(tamanio_sopa_de_letras):
            sopa_de_letras_fila = []
            for j in range(tamanio_sopa_de_letras):
                sopa_de_letras_fila.append(random.choice(letras))
            sopa_de_letras.append(sopa_de_letras_fila)

    def pintar_sopa_de_letras():
        for i in range(len(sopa_de_letras)):
            for j in range(len(sopa_de_letras[i])):
                print(sopa_de_letras[i][j], end=" ")
            print("")

    def meter_palabra_horizontal(palabra):
        fila_aleatoria = random.randint(0, 29)
        columna_aleatoria = random.randint(0, 17)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria][columna_aleatoria + i] = palabra[i]

    def meter_palabra_vertical(palabra):
        fila_aleatoria = random.randint(0, 17)
        columna_aleatoria = random.randint(0, 29)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria + i][columna_aleatoria] = palabra[i]

    def meter_palabra_digonal(palabra):
        fila_aleatoria = random.randint(0, 17)
        columna_aleatoria = random.randint(0, 17)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria + i][columna_aleatoria +
                                               i] = palabra[i]

    palabra = random.choice(palabras)
    llenar_matriz_sopa_de_letras()
    opcion_acomodo = random.randint(0, 3)
    if opcion_acomodo == 0:
        meter_palabra_horizontal(palabra[1])
    elif opcion_acomodo == 1:
        meter_palabra_vertical(palabra[1])
    else:
        meter_palabra_digonal(palabra[1])

    print(
        "ALERTA: Tarea nueva. Para estar más cerca de ganar el juego, necesitas resolver la siguiente tarea. Para hacerlo, tienes que encontrar la respuesta a la pregunta en esta sopa de letras. ¡SUERTE! (recuerda que todo es en minusculas y sin acentos.)\n"
    )

    pintar_sopa_de_letras()
    print()

    print(palabra[0])
    print()
    respuesta = input()
    print()
    if respuesta == palabra[1]:
        print(
            "Ganaste el reto, muy bien, sigue así y al final descubrirás quién es el impostor.\n"
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "Perdiste el reto, lo siento muhco, échale más ganas para que no te descubran. Esta vez elimiaron a "+jugadores[0]+"\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

def sopa_i():
    global gomita
    global jugadores
    global puntos_finales
    global letras
    global sopa_de_letras
    global palabras
    tamanio_sopa_de_letras = 30

    palabras_archivo = open("PalabrasSopaDeLetras.txt", "r")

    for palabra in palabras_archivo:
        palabra_string = palabra.replace("\n", "")
        palabra_list = palabra_string.split(";")
        palabras.append(palabra_list)

    def llenar_matriz_sopa_de_letras():
        for i in range(tamanio_sopa_de_letras):
            sopa_de_letras_fila = []
            for j in range(tamanio_sopa_de_letras):
                sopa_de_letras_fila.append(random.choice(letras))
            sopa_de_letras.append(sopa_de_letras_fila)

    def pintar_sopa_de_letras():
        for i in range(len(sopa_de_letras)):
            for j in range(len(sopa_de_letras[i])):
                print(sopa_de_letras[i][j], end=" ")
            print("")

    def meter_palabra_horizontal(palabra):
        fila_aleatoria = random.randint(0, 29)
        columna_aleatoria = random.randint(0, 17)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria][columna_aleatoria + i] = palabra[i]

    def meter_palabra_vertical(palabra):
        fila_aleatoria = random.randint(0, 17)
        columna_aleatoria = random.randint(0, 29)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria + i][columna_aleatoria] = palabra[i]

    def meter_palabra_digonal(palabra):
        fila_aleatoria = random.randint(0, 17)
        columna_aleatoria = random.randint(0, 17)

        for i in range(len(palabra)):
            sopa_de_letras[fila_aleatoria + i][columna_aleatoria +
                                               i] = palabra[i]

    palabra = random.choice(palabras)
    llenar_matriz_sopa_de_letras()
    opcion_acomodo = random.randint(0, 3)
    if opcion_acomodo == 0:
        meter_palabra_horizontal(palabra[1])
    elif opcion_acomodo == 1:
        meter_palabra_vertical(palabra[1])
    else:
        meter_palabra_digonal(palabra[1])

    print(
        "ALERTA: Tarea nueva. Para estar más cerca de ganar el juego, necesitas resolver la siguiente tarea. Para hacerlo, tienes que encontrar la respuesta a la pregunta en esta sopa de letras. ¡SUERTE! (recuerda que todo es en minusculas y sin acentos.)\n"
    )

    pintar_sopa_de_letras()
    print()

    print(palabra[0])
    print()
    respuesta = input()
    print()
    if respuesta == palabra[1]:
        print(
            "Excelente, ganaste este reto, ahora eliminaste a "+jugadores[0]+", sigue así para eliminar a todos en la nave\nTodavía quedan ellos:\n "
        )
        gomita = 1
        puntos_finales += 1
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])
    else:
        print(
            "Perdiste este reto, casi te cachan y te expulsan, pon atención a la próxima, si no, bye bye.\nLograste eliminar a "+jugadores[0]+"\nTodavía quedan ellos:\n"
        )
        del jugadores[0]
        for i in range(0, len(jugadores)):
            print(jugadores[i])

# Funciones para adivinar impostor 

def adivinar1():
    global jugadores
    global acabar
    adivinar_jugador1 = input(
        "\n¡Excelente! Has completado 3 tareas sin que nadie te mate. Por eso, te queremos dar una pista para que puedas adivinar quién es el impostor.\n PISTA: No es nombre de persona real.\n Ingresa el tripulante que crees que sea el impostor.\n\n"
    )
    while adivinar_jugador1 not in jugadores:
      adivinar_jugador1= input("\nNo existe ese jugador, ingresa un nombre válido.\n\n")
    if adivinar_jugador1 == "cheeto":
        acabar = 1
    else:
        print(
            "\nNo has adivinado, " + adivinar_jugador1 +
            " NO ERA UN IMPOSTOR, sigue con el juego, sigue intentando\nTodavía quedan ellos:\n"
        )
        jugadores.remove(adivinar_jugador1)
        for i in range(0, len(jugadores)):
            print(jugadores[i])        

def adivinar2():
    global jugadores
    global acabar
    adivinar_jugador2 = input(
        "\n¡Excelente! Has completado otras 3 tareas sin que nadie te mate. Por eso, te queremos dar una pista para que puedas adivinar quién es el impostor.\nPISTA: El nombre del impostor tiene una letra 'e'.\nIngresa el tripulante que crees que sea el impostor.\n\n"
    )
    while adivinar_jugador2 not in jugadores:
      adivinar_jugador2= input("\nNo existe ese jugador, ingresa un nombre válido.\n\n")
    if adivinar_jugador2 == "cheeto":
        acabar = 1
    else:
        print(
            "\nNo has adivinado, " + adivinar_jugador2 +
            " NO ERA UN IMPOSTOR, sigue con el juego, sigue intentando\nTodavía quedan ellos:\n"
        )
        jugadores.remove(adivinar_jugador2)
        for i in range(0, len(jugadores)):
            print(jugadores[i])
        
def adivinar3():
    global jugadores
    global acabar
    adivinar_jugador3 = input(
        "\n¡Excelente! Has completado más tareas sin que nadie te mate. Por eso, te queremos dar una pista para que puedas adivinar quién es el impostor.\n PISTA: El nombre del impostor tiene 6 caracteres.\nIngresa el tripulante que crees que sea el impostor.\n\n"
    )
    while adivinar_jugador3 not in jugadores:
      adivinar_jugador3= input("\nNo existe ese jugador, ingresa un nombre válido.\n\n")
    if adivinar_jugador3 == "cheeto":
        acabar = 1
    else:
        print(
            "\nNo has adivinado, " + adivinar_jugador3 +
            " NO ERA UN IMPOSTOR, sigue con el juego, sigue intentando\nTodavía quedan ellos:\n"
        )
        jugadores.remove(adivinar_jugador3)
        for i in range(0, len(jugadores)):
            print(jugadores[i])
        
def adivinar4():
    global jugadores
    global acabar
    adivinar_jugador4 = input(
        "\n¡Tienes una de las últimas oportunidades para que puedas adivinar quién es el impostor!\n PISTA: Es algo que nos gusta a muchos.\nIngresa el tripulante que crees que sea el impostor.\n\n"
    )
    while adivinar_jugador4 not in jugadores:
      adivinar_jugador4= input("\nNo existe ese jugador, ingresa un nombre válido.\n\n")
    if adivinar_jugador4 == "cheeto":
        acabar = 1
    else:
        print(
            "\nNo has adivinado, " + adivinar_jugador4 +
            " NO ERA UN IMPOSTOR, sigue con el juego, sigue intentando\nTodavía quedan ellos:\n"
        )
        jugadores.remove(adivinar_jugador4)
        for i in range(0, len(jugadores)):
            print(jugadores[i])
        
def adivinar5():
    global jugadores
    adivinar_jugador5 = input(
        "\n¡Tienes la última oportunidad para que puedas adivinar quién es el impostor!\n PISTA: En la vida real es del mismo color que el de una fruta que lleva el nombre de su color.\n Ingresa el tripulante que crees que sea el impostor.\n\n"
    )
    while adivinar_jugador5 not in jugadores:
      adivinar_jugador5= input("\nNo existe ese jugador, ingresa un nombre válido.\n\n")
    if adivinar_jugador5 == "cheeto":
        print(
            "\nLo lograste, entre tú y los últimos tripulantes lograron descubrir a cheeto y lograron expulsarlo de la nave.\n¡Felicidades! Has ganado el Juego."
        )
        print("Tuviste " + str(puntos_finales) + " preguntas correctas de 15.")
    else:
        print(
            "\nCasi lo logras, estuviste a punto de expulsar al impostor, pero logró convencer a los últimos tripulantes de votar por expulsarte a ti y ya logró eliminar a todos. El impostor era cheeto.\nLamentablemente... Has perdido el Juego.\n"
        )
        print("Tuviste " + str(puntos_finales) + " preguntas correctas de 15.")

# Función del juego

def jugar():
    global final
    global acabar
    global nombre
    global opcion
    while True:
        color = input(
            "\n" + str(nombre) +
            " escoge tu color:\n\n 1) Negro\n 2) Blanco\n 3) Rosa\n 4) Amarillo\n 5) Cian\n 6) Morado\n 7) Naranja\n 8) Café\n 9) Verde Claro\n 10) Azul fuerte\n 11) Rojo\n 12) Gris\n 13) Dorado\n 14) Plateado\n 15) Magenta\n 16) Salmón\n\n"
        )
        if color.isdecimal() and int(color) <= 16:
            break
        else:
            print("\nDebes Ingresar un número entre 1 y 16.\n")
        print()

    if opcion == "Tripulante":
        while True:
            print(
                "\nBienvenido " + str(nombre) +
                ", eres un TRIPULANTE. la nave en la que estás viajando está siendo saboteada por un impostor que se encuentra entre todos nosotros. Tu trabajo es acabar todas las tareas y descubrir quién es el impostor. Cada pregunta correcta es una tarea completada. Hay preguntas de opción múltiple en las cuales tendrás que ingresar el número de la opción correcta, hay preguntas abiertas en las cuales tendras que escribir la respuesta correcta, y hay minijuegos, los cuales incluyen instrucciones sobre como jugarlos. Recuerda que debes evitar que te maten. ¡SUERTE!\nHay un impostor entre todos nosotros:\n"
            )
            for i in range(len(jugadores)):
              print(jugadores[i])
            #1
            preguntar_op_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #2
            preguntar_abiertas_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #3
            preguntar_abiertas_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #4
            ahorcado_1_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break

            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #5
            sopa_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #6
            preguntar_op_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #7
            preguntar_abiertas_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #8
            preguntar_op_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #9
            ahorcado2_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break

            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #10
            sopa_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #11
            preguntar_op_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #12
            preguntar_abiertas_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 12:
                adivinar4()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #13
            sopa_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 12:
                adivinar4()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #14
            preguntar_op_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 12:
                adivinar4()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            input(
                "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
            )
            #15 
            ahorcado3_t()
            print()
            print("Tu puntuación es: " + str(puntos_finales))
            print()
            if puntos_finales == 3:
                adivinar1()
                if acabar == 1:
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    final = 1
                    break
            elif puntos_finales == 6:
                adivinar2()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 9:
                adivinar3()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            elif puntos_finales == 12:
                adivinar4()
                if acabar == 1:
                    final = 1
                    print(
                        "Adivinaste, cheeto SI ERA EL IMPOSTOR, ganaste el juego"
                    )
                    break
            if puntos_finales >= 10:
              adivinar5()
            else:
              print(
                    "\nCasi lo logras, estuviste a punto de expulsar al impostor, pero logró convencer a los últimos tripulantes de votar por expulsarte a ti y ya logró eliminar a todos. El impostor era cheeto.\nLamentablemente... Has perdido el Juego.\n"
                   )
              print("Tuviste " + str(puntos_finales) + " preguntas correctas de 15.")   
            break

    if opcion == "Impostor":
        print(
            "\nBienvenido " + str(nombre) +
            ", eres el IMPOSTOR. Tu trabajo es sabotear la nave y matar a todos los tripulantes. Cada pregunta correcta es alguien menos en tu lista de matanza. Hay preguntas de opción múltiple en las cuales tendrás que ingresar el número de la opción correcta, hay preguntas abiertas en las cuales tendras que escribir la respuesta correcta, y hay minijuegos, los cuales incluyen instrucciones sobre como jugarlos. Recuerda, que no sospechen de ti. ¡SUERTE!\nTienes que eliminar a todos ellos, menos a ti mismo:\n"
        )
        for i in range(len(jugadores)):
          print(jugadores[i])

        preguntar_op_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_abiertas_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_abiertas_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        ahorcado_1_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        sopa_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_op_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_abiertas_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_op_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        ahorcado2_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        sopa_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_op_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_abiertas_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        sopa_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        preguntar_op_i()
        print()
        print("Tu puntuación es: " + str(puntos_finales))
        print()
        input(
            "\n¿Estas listo para la siguiente Pregunta?\nSi ya estas listo, dale ENTER para continuar.\n"
        )
        ahorcado3_i()
        if puntos_finales >= 10:
            print(
                "\nLo lograste, pudiste covencer a uno de los dos útlimos tripulantes de expulsar al otro tripulante. La nave es toda tuya, por lo tanto lograste eliminar a todos los tripulantes. Eres un Gran IMPOSTOR.\n¡Felicidades! Has ganado el Juego."
            )
            
        else:
            print(
                "\nCasi lo logras, estuviste a punto de eliminar a los dos últimos tripulantes pero al final te expulsaron a ti de la nave. A la próxima no dejes tantas pistas de que eres el impostor y sé más cauteloso.\nLamentablemente... Has perdido el Juego."
            )
        print("Tuviste " + str(puntos_finales) + " preguntas correctas de 15.")

# While para ejecutar el juego y volver a jugar o acabar

while True:
    jugar()
    volver_a_jugar = str(input("\n¿Quieres volver a jugar?\n1) Sí\n2) No\n"))
    while volver_a_jugar != "1" and volver_a_jugar != "2":
      print("\nSolo puedes ingresar 1 ó 2\n")
      volver_a_jugar = str(input("\n¿Quieres volver a jugar?\n1) Sí\n2) No\n"))
    if volver_a_jugar == "2":
        break
    if volver_a_jugar == "1":
        print("\nComencemos de nuevo " + str(nombre) + ".")
        puntos_finales=0