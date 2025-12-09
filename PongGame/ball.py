"""
ball.py - Clase Ball (Pelota)

Este módulo define la clase Ball que representa la pelota del juego Pong.
Hereda de Turtle para aprovechar sus capacidades gráficas y de movimiento.
"""

from turtle import Turtle


class Ball(Turtle):
    """
    Clase que representa la pelota del juego Pong.
    
    La pelota se mueve diagonalmente y puede rebotar en las paredes
    y paletas. La velocidad aumenta cada vez que golpea una paleta.
    
    Atributos:
        x_move (int): Velocidad de movimiento horizontal (positivo = derecha)
        y_move (int): Velocidad de movimiento vertical (positivo = arriba)
        move_speed (float): Factor de velocidad del juego (menor = más rápido)
    """

    def __init__(self):
        """Inicializa la pelota con su apariencia y velocidad inicial."""
        super().__init__()
        self.color("white")  # Color blanco para contrastar con fondo negro
        self.shape("circle")  # Forma circular
        self.penup()  # No dibujar líneas al moverse
        self.x_move = 3  # Velocidad horizontal inicial
        self.y_move = 3  # Velocidad vertical inicial
        self.move_speed = 0.1  # Velocidad base del juego

    def move(self):
        """
        Mueve la pelota según su velocidad actual.
        
        Calcula la nueva posición sumando x_move e y_move
        a las coordenadas actuales.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Hace que la pelota rebote verticalmente.
        
        Invierte la dirección vertical multiplicando y_move por -1.
        Se llama cuando la pelota toca la pared superior o inferior.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Hace que la pelota rebote horizontalmente y aumenta la velocidad.
        
        Invierte la dirección horizontal y reduce move_speed en un 10%
        para hacer el juego más difícil progresivamente.
        Se llama cuando la pelota golpea una paleta.
        """
        self.x_move *= -1
        self.move_speed *= 0.9  # Aumenta la velocidad (menor delay)

    def reset_position(self):
        """
        Reinicia la pelota al centro de la pantalla.
        
        Se llama cuando un jugador anota un punto.
        Restablece la velocidad del juego y cambia la dirección
        para que la pelota vaya hacia el jugador que anotó.
        """
        self.goto(0, 0)  # Volver al centro
        self.move_speed = 0.1  # Reiniciar velocidad
        self.bounce_x()  # Cambiar dirección hacia el otro lado
