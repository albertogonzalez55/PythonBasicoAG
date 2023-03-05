


import random
import time
#Definiendo variables
suits = ("Espadas", "Trebol", "Corazones", "Diamantes")
ranks = ( "1","2","3","4","5","6","7","8","9","10","J","Q","K","A",)
#Estas son para dar un valor numerico a las cartas para realizar operaciones luego.
valores = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10,"A": 11,}



playing = True

opcion = input("Digita una opcion entre 1 y 3. 1= Iniciar Partida 3= Salir: ")
while opcion.lower() not in ["1", "2"]:
    if opcion == '1':
      playing =True      
    elif opcion == "3":  
        print("\n------------------------Gracias por jugar!---------------------\n")
    break
# Derfiniendo las clases:


#Esta es la clase carta
class Card:
    def __init__(self, suit, rank): #Método init para inicializar atributos
       #Atributos de instancia
       # Suit son la categoría de carta Espadas,trebol,corazones...
       # Rank es el numero de carta 1,2,3,4,J,Q,K... 
        self.suit = suit
        self.rank = rank

#Define un string que el sistema imprime para explicar al jugador
#  que carta con que categoría le salió
    def __str__(self):
        return self.rank + " de " + self.suit

#Clase para inicializar el mazo de cartas.
class Deck:
    def __init__(self):
        self.deck = [] #El mazo inicia vacio 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) #Agrega el numero y categoría de carta

    def __str__(self):
        deck_comp = "" 
        for card in self.deck:
            deck_comp += "\n " + card.__str__()  
        return "El mazo tiene:" + deck_comp

#Función para que la carta y categoría sean aleatorias.
    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Inicializa la clase de la mano
class Hand:
    def __init__(self):
        self.cards = []  # Inicia con la lista vacía
        self.value = 0  
        self.aces = 0  #Para contar la cantidad de "A"

#Agrega la carta a la mano, si la carta es un A suma uno a la variable self.aces 
    def add_card(self, card):
        self.cards.append(card)
        self.value += valores[card.rank]
        if card.rank == "A":
            self.aces += 1  

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#Funciones de juego
#Al iniciar el juego esta función agrega una carta a cada jugador.
def hit(deck, mano):
    mano.add_card(deck.deal())
    mano.adjust_for_ace()


def hit_or_stand(deck, hand):#Esta función pregunta al jugador si quiere mantenerse o pedir otra carta
    global playing
    while True:#Mientras sea true el sistema se mantiene dando cartas al jugador hasta pasarse de 21
        x = input("\nTe gustaría pedir o mantener el mazo así? Presiona [p/m] y luego Enter: ")

#Esto es para recibir información del teclado en este caso si el jugador presiona p de "pedir"
        if x[0].lower() == "p":
            hit(deck, hand)  

#Esto es para recibir información del teclado en este caso si el jugador presiona m de "mantener"
        elif x[0].lower() == "m":
            print("El jugador se mantiene. Turno del segundo jugador")
            playing = False #Aquí se llama a false para salir del bucle y continuar.

        else:
            print("Tecla errónea favor preciona p o m")
            continue
        break

#Funciones para hacer el display de las manos de los jugadores con la carta secreta de la computadora

#Enseñaer algunas
def show_algunas(jugador, dealer):
    print("\nMano del jugador:", *jugador.cards, sep="\n ")
    print("Mano del Jugador =", jugador.value)
    print("\nMano de la Computadora:")
    print(" <Carta Secreta>")
    print("", dealer.cards[1])

#Esta Muestra los resultados al final con todas las cartas incluidas.
def show_todas(jugador, dealer):
    print("\nMano del jugador:", *jugador.cards, sep="\n ")
    print("Mano del jugador =", jugador.value)
    print("\nMano de la Computadora:", *dealer.cards, sep="\n ")
    print("Mano de la Computadora =", dealer.value)

#Si el jugador pierde:
def jugador_pierde(jugador, dealer):
    print("\Jugador perdió")

#Jugador gana:
def jugador_gana(jugador, dealer):
    print("\nJugador hizo Blackjack, HAS GANADO")

#Dealer pierde:
def dealer_pierde(jugador, dealer):
    print("\nDelear perdió")

#Dealer gana:
def dealer_gana(jugador, dealer):
    print("\nDealer ganó")


def push(jugador, dealer):
    print("\nEMPATE")

while True:
    # Introducción del jugador 
    print("Blackjack")
    # Craer y barajar las cartas
    deck = Deck()
    deck.shuffle()
    # Dos cartas a cada jugador
    mano_jugador = Hand()
    mano_jugador.add_card(deck.deal())
    mano_jugador.add_card(deck.deal())

    mano_dealer = Hand()
    mano_dealer.add_card(deck.deal())
    mano_dealer.add_card(deck.deal())

    # Darle la vuelta a las cartas (enseñaelas)
    show_algunas(mano_jugador, mano_dealer)

    while playing:  # Usar variable

        # Preguntar al jugador si atacar o quedarse
        hit_or_stand(deck, mano_jugador)
        show_algunas(mano_jugador, mano_dealer)

        #Verificar si es mayor a 21
        if mano_jugador.value > 21:
            jugador_pierde(mano_jugador, mano_dealer)
            break

    # Si jugador no ha perdido, jugar con el dealer
    if mano_jugador.value <= 21:

        while mano_dealer.value < 17:
            hit(deck, mano_dealer)

        # Darle la vuelta a todas las cartas (enseñarlas)
        time.sleep(1)
        print("Resultados")

        show_todas(mano_jugador, mano_dealer)

        # Probar con distintoss "filtros" ver si gano:
        if mano_dealer.value > 21:
            dealer_pierde(mano_jugador, mano_dealer)

        elif mano_dealer.value > mano_jugador.value:
            dealer_gana(mano_jugador, mano_dealer)

        elif mano_dealer.value < mano_jugador.value:
            jugador_gana(mano_jugador, mano_dealer)

        else:
            push(mano_jugador, mano_dealer)

    # Preguntar al usuario si quiere jugar otra vez
    juego_nuevo = input("\nJugar con la otra mano [Y/N] ")
    while juego_nuevo.lower() not in ["y", "n"]:
        juego_nuevo = input("Invalido")
    if juego_nuevo[0].lower() == "y":
        playing = True
        continue

    # Sino agradecer al jugador por jugar
    else:
        print("Gracias por jugar")
        break