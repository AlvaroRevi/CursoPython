"""
paddle.py - Clase Paddle (Paleta)

Este módulo define la clase Paddle que representa las paletas de los jugadores.
Hereda de Turtle para aprovechar sus capacidades gráficas.
"""

from turtle import Turtle


class Paddle(Turtle):
    """
    Clase que representa una paleta del juego Pong.
    
    Cada paleta puede moverse verticalmente (arriba/abajo) para
    intentar golpear la pelota y evitar que pase.
    
    Atributos heredados de Turtle:
        - Posición (x, y)
        - Forma y color
    """

    def __init__(self, position):
        """
        Inicializa la paleta con su apariencia y posición.
        
        Args:
            position (tuple): Coordenadas (x, y) donde colocar la paleta.
                             Típicamente (350, 0) para derecha o (-350, 0) para izquierda.
        """
        super().__init__()
        self.shape("square")  # Forma cuadrada base
        self.color("white")  # Color blanco
        # Estira el cuadrado: 5x alto (100px), 1x ancho (20px)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()  # No dibujar líneas al moverse
        self.goto(position)  # Colocar en la posición inicial

    def go_up(self):
        """
        Mueve la paleta hacia arriba.
        
        Aumenta la coordenada Y en 20 píxeles, manteniendo
        la misma coordenada X.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Mueve la paleta hacia abajo.
        
        Disminuye la coordenada Y en 20 píxeles, manteniendo
        la misma coordenada X.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
