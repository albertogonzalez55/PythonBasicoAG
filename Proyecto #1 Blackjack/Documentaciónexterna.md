Por Valerie Calvo y Alberto González

## DOCUMENTACIÓN EXTERNA

**Introducción:**
Este es un código de un juego de blackjack en Python. Este posee un menú de opciones en el que el usuario decide si Iniciar un juego y escribir su nombre, si desea ver sus resultados anteriores y si quiere salirse. 

**Manual de usuario:**
1-	El usuario elige una de las opciones, si elige la opción uno el juego comienza.
2-	Lo primero es ingresar el nombre de usuario para ser diferenciado de la computadora, el usuario simplemente debe elegir un nombre y apretar “Enter”
3-	El juego automáticamente iniciará y al azar repartirán las cartas 2 para el usuario que se mostrarán en pantalla y dos de la computadora o del sistema con la excepción de que solo se mostrará una y la otra se mantendrá en secreto.
4-	El sistema preguntará al usuario si quiere pedir otra carta o mantenerse con las que ya tiene. El usuario debe escribir “p” si quiere pedir otra carta o “m” si quiere mantener y luego “Enter”.
5-	Sea lo que decida el sistema empezará a sumar los valores de las cartas en total y decidirá al ganador. El jugador que este más cerca del número 21 será el ganador, en caso de que los dos resultados sean iguales se declarará un empate y si alguno de los dos se para del número 21 perderá automáticamente la partida.
6-	Al declarar el ganador el sistema lanzará una pregunta por si el usuario desea seguir jugando. Si no lo desea debe escribir “n” y si lo desea presionar “s” y “Enter”.

**Información técnica del programa:**
El código incluye las siguientes clases y funciones:
1. **suits:** Una tupla que contiene los cuatro tipos de diseño de la baraja: espadas, tréboles, corazones y diamantes.
2. **ranks:** Una tupla que contiene las cartas de la baraja con sus respectivos valores: del 1 al 10, J, Q, K y A.
3. **valores:** Un diccionario que asocia a cada carta su respectivo valor numérico. Por ejemplo, que la K vale 10.
4. **playing:** Una variable booleana que indica si el juego sigue en marcha o no. 
opcion: Una variable que se utiliza para que el jugador pueda elegir entre iniciar una partida o salir del juego.
5. **Card:** Una clase que representa una carta de la baraja. Cada objeto Card tiene dos atributos: suit (el tipo de diseño de la carta) y rank (el valor numérico de la carta).
6. **Deck:** Una clase que representa el mazo de cartas. Cada objeto Deck se compone de una lista de objetos Card.
7. **Hand:** Una clase que representa la mano de un jugador. Cada objeto Hand se compone de una lista de objetos Card, un valor numérico que representa la suma de los valores de las cartas de la mano, y una variable que cuenta la cantidad de ases que tiene la mano.
8. **hit():** Una función que toma un objeto Deck y un objeto Hand como argumentos, y añade una carta al objeto Hand.
9. **hit_or_stand():** Una función que toma un objeto Deck y un objeto Hand como argumentos, y permite al jugador elegir si quiere pedir otra carta o mantener su mano actual.
10. **show_algunas():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra al jugador las cartas que tiene en su mano y la carta visible del crupier.
11. **show_todas():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra al jugador todas las cartas que hay en juego.
12. **jugador_pierde():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra un mensaje indicando que el jugador ha perdido.
13. **jugador_gana():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra un mensaje indicando que el jugador ha ganado.
14. **Deck.shuffle():** Una función que mezcla el mazo de cartas.
15. **Deck.deal():** Una función que saca una carta del mazo.
16. **Dealer.pierde():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra un mensaje indicando que el dealer ha perdido.
17. **Dealer.gana():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra un mensaje indicando que el dealer ha ganado.
18. **push():** Una función que toma dos objetos Hand como argumentos (la mano del jugador y la mano del crupier), y muestra un mensaje indicando que es un empate
19.**while True** = empieza el juego
20. **deck.shuffle ():** mezclar aleatoriamente el deck
21. **.addcard():** agregar dos cartas a cada jugador
