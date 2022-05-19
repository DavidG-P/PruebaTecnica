from clases.preguntas import Pregunta
from clases.respuestas import Respuesta
import sqlite3

contadorPreguntas = 0
puntos = 0

#CREAR PREGUNTAS
p1 = Pregunta(1,"En qué año fue el descubrimiento de América?",1,1)
p2 = Pregunta(2,"Cuál es el país con mayor población del mundo?",1,1)
p3 = Pregunta(3,"Cuál era el nombre del dios del Sol en el Antiguo Egipto?",1,1)
p4 = Pregunta(4,"Quién fue el primer presidente de Estados Unidos?",1,1)
p5 = Pregunta(5,"Quién es el autor de La Odisea?",1,1)

p6 = Pregunta(6,"Cómo se llama el estadio de fútbol del Real Madrid?",2,2)
p7 = Pregunta(7,"En qué deporte destaca Tiger Woods?",2,2)
p8 = Pregunta(8,"Quién ganó el mundial de de fútbol del año 2014?",2,2)
p9 = Pregunta(9,"De que país es el futbolista Radamel Falcao Garcia?",2,2)
p10 = Pregunta(10,"En qué equipo jugó Francesco Totti durante toda su carrera?",2,2)

p11 = Pregunta(11,"Cuál es el río más largo del mundo?",3,3)
p12 = Pregunta(12,"Cuál es el océano más grande del mundo?",3,3)
p13 = Pregunta(13,"Cuántos lados tiene un heptágono?",3,3)
p14 = Pregunta(14,"Cuál es el planeta más grande del Sistema Solar?",3,3)
p15 = Pregunta(15,"Cuántos huesos tiene el cuerpo humano?",3,3)

p16 = Pregunta(16,"Cuántos corazones tiene un gusano de tierra?",4,4)
p17 = Pregunta(17,"Cuántos días tiene un año bisiesto??",4,4)
p18 = Pregunta(18,"Cuántas patas tiene una araña?",4,4)
p19 = Pregunta(19,"Cuántos corazones tiene un pulpo?",4,4)
p20 = Pregunta(20,"Cuanto es 10+80 ?",4,4)

p21 = Pregunta(21,"Cuántas horas tiene un día ?",5,5)
p22 = Pregunta(22,"Cuantos minutos tiene una hora ?",5,5)
p23 = Pregunta(23,"Cuantos departamentos tiene Colombia ?",5,5)
p24 = Pregunta(24,"Cuantas son las ramas del poder público en Colombia ?",5,5)
p25 = Pregunta(25,"Cual es la capital de Colombia ?",5,5)

#crear respuestas

r1 = Respuesta(1,"(1492)",1,True)
r2 = Respuesta(2,"(1342)",1,False)
r3 = Respuesta(3,"(1429)",1,False)
r4 = Respuesta(4,"(1352)",1,False)

r5 = Respuesta(5,"(Perú)",2,False)
r6 = Respuesta(6,"(Colombia)",2,False)
r7 = Respuesta(7,"(China)",2,True)
r8 = Respuesta(8,"(Uruguay)",2,False)

r9 = Respuesta(9,"(Odín)",3,False)
r10 = Respuesta(10,"(Ra)",3,True)
r11 = Respuesta(11,"(platón)",3,False)
r12 = Respuesta(12,"(David)",3,False)

r13 = Respuesta(13,"(Álvaro Uribe)",4,False)
r14 = Respuesta(14,"(George Washington)",4,True)
r15 = Respuesta(15,"(Simón Bolívar)",4,False)
r16 = Respuesta(16,"(Elkin Patarroyo)",4,False)

r17 = Respuesta(17,"(benjamín)",5,False)
r18 = Respuesta(18,"(Simón)",5,False)
r19 = Respuesta(19,"(Alberto)",5,False)
r20 = Respuesta(20,"(Homero)",5,True)

r21 = Respuesta(21,"(Santiago Bernabéu) ",6,True)
r22 = Respuesta(22,"(Wanda Metropolitano)",6,False)
r23 = Respuesta(23,"(Camp Nou)",6,False)
r24 = Respuesta(24,"(San Mames)",6,False)

r25 = Respuesta(25,"((Futbol))",7,False)
r26 = Respuesta(26,"((Natación))",7,False)
r27 = Respuesta(27,"(vóleibol)",7,False)
r28 = Respuesta(28,"(Golf)",7,True)

r29 = Respuesta(29,"(Perú)",8,False)
r30 = Respuesta(30,"(China)",8,False)
r31 = Respuesta(31,"(España)",8,False)
r32 = Respuesta(32,"(Alemania)",8,True)

r33 = Respuesta(33,"(Colombia)",9,True)
r34 = Respuesta(34,"(Chile)",9,False)
r35 = Respuesta(35,"(Ecuador)",9,False)
r36 = Respuesta(36,"(Alemania)",9,False)

r37 = Respuesta(37,"(AC Milán)",10,False)
r38 = Respuesta(38,"(Juventus FC)",10,False)
r39 = Respuesta(39,"(S.S Lazio)",10,False)
r40 = Respuesta(40,"(AS Roma)",10,True)

r41 = Respuesta(41,"(Nilo)",11,False)
r42 = Respuesta(42,"(Amazonas)",11,True)
r43 = Respuesta(43,"(Congo)",11,False)
r44 = Respuesta(44,"(Misisipi)",11,False)

r45 = Respuesta(45,"(Atlántico)",12,False)
r46 = Respuesta(46,"(Indico)",12,False)
r47 = Respuesta(47,"(océano Pacífico)",12,True)
r48 = Respuesta(48,"(Ártico)",12,False)

r49 = Respuesta(49,"(Siete lados) ",13,True)
r50 = Respuesta(50,"(Seis lados)",13,False)
r51 = Respuesta(51,"(Cinco lados)",13,False)
r52 = Respuesta(52,"(Diez lados)",13,False)


r53 = Respuesta(53,"(Plutón)",14,False)
r54 = Respuesta(54,"(Júpiter)",14,True)
r55 = Respuesta(55,"(Urano)",14,False)
r56 = Respuesta(56,"(Neptuno)",14,False)

r57= Respuesta(57,"(206)",15,True)
r58= Respuesta(58,"(300)",15,False)
r59= Respuesta(59,"(400)",15,False)
r60= Respuesta(60,"(150)",15,False)

r61= Respuesta(61,"(Dos)",16,False)
r62= Respuesta(62,"(Quince)",16,False)
r63= Respuesta(63,"(Cinco)",16,True)
r64= Respuesta(64,"(Diez)",16,False)

r65= Respuesta(65,"(380 días)",17,False)
r66= Respuesta(66,"(300 días)",17,False)
r67= Respuesta(67,"(400 días)",17,False)
r68= Respuesta(68,"(366 días)",17,True)

r69= Respuesta(69,"(Ocho)",18,True)
r70= Respuesta(70,"(Dos)",18,False)
r71= Respuesta(71,"(Diez)",18,False)
r72= Respuesta(72,"(Cinco)",18,False)

r73= Respuesta(73,"(Un corazón)",19,False)
r74= Respuesta(74,"(Dos corazones)",19,False)
r75= Respuesta(75,"(Tres corazones)",19,True)
r76= Respuesta(76,"(Cinco corazones)",19,False)

r77= Respuesta(77,"(70)",20,False)
r78= Respuesta(78,"(90)",20,True)
r79= Respuesta(79,"(100)",20,False)
r80= Respuesta(80,"(60)",20,False)

r81= Respuesta(81,"(20 Horas)",21,False)
r82= Respuesta(82,"(15 Horas)",21,False)
r83= Respuesta(83,"(12 Horas)",21,False)
r84= Respuesta(84,"(24 Horas)",21,True)

r85= Respuesta(85,"(50 minutos)",22,False)
r86= Respuesta(86,"(40 minutos)",22,False)
r87= Respuesta(87,"(60 minutos",22,True)
r88= Respuesta(88,"(24 Minutos)",22,False)

r89= Respuesta(89,"(20)",23,False)
r90= Respuesta(90,"(32)",23,True)
r91= Respuesta(91,"(40)",23,False)
r92= Respuesta(92,"(24)",23,False)

r93= Respuesta(93,"(Tres)",24,True)
r94= Respuesta(94,"(Cuatro)",24,False)
r95= Respuesta(95,"(Cinco)",24,False)
r96= Respuesta(96,"(Diez)",24,False)

r97= Respuesta(97,"(Pereira)",25,False)
r98= Respuesta(98,"(Cali)",25,False)
r99= Respuesta(99,"(Bogota)",25,True)
r100= Respuesta(100,"(Barranquilla)",25,False)


#lista de preguntas
preguntas = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25]
# lista de respuestas
respuestas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,
    r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36,r37,r38,r39,r40,
    r41,r42,r43,r44,r45,r46,r47,r48,r49,r50,r51,r52,r53,r54,r55,r56,r57,r58,r59,r60,r61,r62,r63,
    r64,r65,r66,r67,r68,r69,r70,r71,r72,r73,r74,r75,r76,r77,r78,r79,r80,r81,r82,r83,r84,r85,r86,r87,r88,r89,r90,
    r91,r92,r93,r94,r95,r96,r97,r98,r99,r100]


print("Jugar")

# datos del jugador
nombres = input("registrar nombres:")
apellidos = input("registrar apellidos:")

#funcion  retorna las respuestas de la pregunta
def dimeRespuestas(preguntaId):
    lista = []
    for r in respuestas:
        if r.dime_preguntaId() == preguntaId:
            lista.append(r)
    return lista 

# Se crea en la raiz, la base de datos "historico_jugador" al finalizar la ejecucion del programa.
def guardar(nom,apell,puntaje):
    conexion = sqlite3.connect("historico_jugador")
    cursor = conexion.cursor()
    sql = "CREATE TABLE IF NOT EXISTS HISTORICO (NOMBRE VARCHAR(50),APELLIDO VARCHAR(50),PUNTAJE INTEGER)"
    cursor.execute(sql)
    insert = "INSERT INTO HISTORICO VALUES (?,?,?)"
    jugador = [(nom,apell,puntaje)]
    cursor.executemany(insert,jugador)
    conexion.commit()
    cursor.close()

for i in preguntas:
    contadorPreguntas +=1
    print("Pregunta ", contadorPreguntas)
    print("Categoria ", i.dime_categoria())
    print(i.dime_descripcion())
    print("RESPUESTAS")
    #buscar pregunta
    respuestaOpciones = dimeRespuestas(i.dime_id())
    print("A:",respuestaOpciones[0].dime_opcion())
    print("B:",respuestaOpciones[1].dime_opcion())
    print("C:",respuestaOpciones[2].dime_opcion())
    print("D:",respuestaOpciones[3].dime_opcion())
    A = respuestaOpciones[0].dime_isTrue()
    B = respuestaOpciones[1].dime_isTrue()
    C = respuestaOpciones[2].dime_isTrue()
    D = respuestaOpciones[3].dime_isTrue()
    opcionSeleccionada =  input("ESCRIBA LA RESPUESTA: (A,B,C,D):")
    if contadorPreguntas <= 5:
        if opcionSeleccionada.upper() == "A":
            if A:
                print("Correcto!")
                puntos += 1
                print("Puntos:",puntos)
               
            else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break       
        elif opcionSeleccionada.upper() == "B":
             if B:
                print("Correcto!")
                puntos += 1
                print("Puntos:",puntos)
                
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "C":
             if C:
                print("Correcto!")
                puntos += 1
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "D":
             if D:
                print("Correcto!")
                puntos += 1
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
    elif contadorPreguntas > 5 and contadorPreguntas <= 10:
        if opcionSeleccionada.upper() == "A":
            if A:
                print("Correcto!")
                puntos += 2
                print("Puntos:",puntos)
                
            else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break       
        elif opcionSeleccionada.upper() == "B":
             if B:
                print("Correcto!")
                puntos += 2
                print("Puntos:",puntos)
                
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "C":
             if C:
                print("Correcto!")
                puntos += 2
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "D":
             if D:
                print("Correcto!")
                puntos += 2
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
    elif contadorPreguntas > 10 and contadorPreguntas <= 15:
        if opcionSeleccionada.upper() == "A":
            if A:
                print("Correcto!")
                puntos += 3
                print("Puntos:",puntos)
            else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break       
        elif opcionSeleccionada.upper() == "B":
             if B:
                print("Correcto!")
                puntos += 3
                print("Puntos:",puntos)
                
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "C":
             if C:
                print("Correcto!")
                puntos += 3
                print("Puntos:",puntos)
               
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "D":
             if D:
                print("Correcto!")
                puntos += 3
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
    elif contadorPreguntas > 15 and contadorPreguntas <= 20:
        if opcionSeleccionada.upper() == "A":
            if A:
                print("Correcto!")
                puntos += 4
                print("Puntos:",puntos)
                
            else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break       
        elif opcionSeleccionada.upper() == "B":
             if B:
                print("Correcto!")
                puntos += 4
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "C":
             if C:
                print("Correcto!")
                puntos += 4
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "D":
             if D:
                print("Correcto!")
                puntos += 4
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
    elif contadorPreguntas > 20 and contadorPreguntas <= 25:
        if opcionSeleccionada.upper() == "A":
            if A:
                print("Correcto!")
                puntos += 5
                print("Puntos:",puntos)
            else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break       
        elif opcionSeleccionada.upper() == "B":
             if B:
                print("Correcto!")
                puntos += 5
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "C":
             if C:
                print("Correcto!")
                puntos += 5
                print("Puntos:",puntos)
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
        elif opcionSeleccionada.upper() == "D":
             if D:
                print("Correcto!")
                puntos += 5
                print("Puntos:",puntos)
                
             else:
                puntos = 0
                print('inCorrecta')
                guardar(nombres,apellidos,puntos)
                break   
    
    if contadorPreguntas == 25:
        print('FELICIDADES TERMINASTE EL JUEGO')
        print("PUNTAJE TOTAL OBTENIDO:", puntos)
        guardar(nombres,apellidos,puntos)
        break
    else:
        respuesta = input('Desea seguir en el juego?: ("SI,NO"):')
        if respuesta.upper() == "NO":
            print('JUEGO TERMINADO')
            print("PUNTAJE OBTENIDO:",puntos)
            guardar(nombres,apellidos,puntos)
            break

    
    
   


    
    
    



