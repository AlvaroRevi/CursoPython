# Importación de librerías necesarias para la interfaz gráfica
from tkinter import *
from quiz_brain import QuizBrain

# Color de tema principal de la aplicación
THEME_COLOR = "#375362"

class QuizInterface:
    """
    Clase que gestiona la interfaz gráfica del juego de trivia.
    Utiliza tkinter para crear una ventana con preguntas y botones de respuesta.
    """
    def __init__(self, quiz_brain: QuizBrain):
        """
        Inicializa la interfaz gráfica del quiz.
        
        Args:
            quiz_brain: Instancia de QuizBrain que contiene la lógica del juego
        """
        self.quiz = quiz_brain
        
        # Crear y configurar la ventana principal
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Etiqueta que muestra la puntuación actual
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas donde se mostrará el texto de la pregunta
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill = THEME_COLOR,
                                                     font = ("Arial",20,"italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # Botón de respuesta "Verdadero"
        true_image = PhotoImage(file="images/true.png")
        self.true_botton = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_botton.grid(row=2, column=0)

        # Botón de respuesta "Falso"
        false_image = PhotoImage(file="images/false.png")
        self.false_botton = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_botton.grid(row=2, column=1)

        # Mostrar la primera pregunta y comenzar el bucle principal
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        Obtiene y muestra la siguiente pregunta en el canvas.
        Si no hay más preguntas, deshabilita los botones y muestra un mensaje final.
        """
        # Restablecer el color de fondo del canvas a blanco
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            # Actualizar la puntuación y mostrar la siguiente pregunta
            self.score_label.config(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Si no hay más preguntas, mostrar mensaje final y deshabilitar botones
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the test")
            self.true_botton.config(state="disabled")
            self.false_botton.config(state="disabled")

    def true_pressed(self):
        """
        Maneja el evento cuando el usuario presiona el botón "Verdadero".
        Verifica la respuesta y muestra el feedback correspondiente.
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """
        Maneja el evento cuando el usuario presiona el botón "Falso".
        Verifica la respuesta y muestra el feedback correspondiente.
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
        Muestra feedback visual al usuario según si la respuesta fue correcta o no.
        Cambia el color del canvas a verde (correcto) o rojo (incorrecto).
        
        Args:
            is_right: Booleano que indica si la respuesta fue correcta
        """
        if is_right:
            # Respuesta correcta: fondo verde
            self.canvas.config(bg="green")
        else:
            # Respuesta incorrecta: fondo rojo
            self.canvas.config(bg="red")
        
        # Esperar 1 segundo antes de mostrar la siguiente pregunta
        self.window.after(1000, self.get_next_question)