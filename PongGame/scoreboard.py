"""
scoreboard.py - Clase Scoreboard (Marcador)

Este módulo define la clase Scoreboard que maneja la puntuación del juego.
Hereda de Turtle para poder dibujar el marcador en pantalla.
"""

from turtle import Turtle


class Scoreboard(Turtle):
    """
    Clase que representa el marcador del juego Pong.
    
    Muestra los puntos de ambos jugadores en la parte superior
    de la pantalla y se actualiza cada vez que alguien anota.
    
    Atributos:
        l_score (int): Puntuación del jugador izquierdo
        r_score (int): Puntuación del jugador derecho
    """

    def __init__(self):
        """Inicializa el marcador con puntuación 0-0."""
        super().__init__()
        self.color("white")  # Color del texto
        self.penup()  # No dibujar líneas
        self.hideturtle()  # Ocultar el cursor de la tortuga
        self.l_score = 0  # Puntos del jugador izquierdo
        self.r_score = 0  # Puntos del jugador derecho
        self.update_scoreboard()  # Mostrar marcador inicial

    def update_scoreboard(self):
        """
        Actualiza la visualización del marcador en pantalla.
        
        Borra el marcador anterior y dibuja los nuevos puntos
        de ambos jugadores en la parte superior de la pantalla.
        """
        self.clear()  # Borrar el marcador anterior
        
        # Mostrar puntuación del jugador izquierdo
        self.goto(-100, 200)  # Posición izquierda superior
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        
        # Mostrar puntuación del jugador derecho
        self.goto(100, 200)  # Posición derecha superior
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Suma un punto al jugador izquierdo.
        
        Se llama cuando la pelota pasa por el lado derecho,
        indicando que el jugador derecho falló.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Suma un punto al jugador derecho.
        
        Se llama cuando la pelota pasa por el lado izquierdo,
        indicando que el jugador izquierdo falló.
        """
        self.r_score += 1
        self.update_scoreboard()