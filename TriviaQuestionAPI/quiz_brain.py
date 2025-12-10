# Importar html para decodificar entidades HTML en las preguntas
import html

class QuizBrain:
    """
    Clase que gestiona la lógica del juego de trivia.
    Maneja las preguntas, respuestas y la puntuación.
    """

    def __init__(self, q_list):
        """
        Inicializa el QuizBrain con una lista de preguntas.
        
        Args:
            q_list: Lista de objetos Question
        """
        self.question_number = 0  # Número de la pregunta actual
        self.score = 0  # Puntuación del usuario
        self.question_list = q_list  # Lista de todas las preguntas
        self.current_question = None  # Pregunta actual que se está mostrando

    def still_has_questions(self):
        """
        Verifica si aún quedan preguntas por responder.
        
        Returns:
            True si hay más preguntas, False en caso contrario
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Obtiene la siguiente pregunta de la lista y la formatea para mostrar.
        Decodifica las entidades HTML en el texto de la pregunta.
        
        Returns:
            String con el número y texto de la pregunta formateado
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Decodificar entidades HTML (como &quot; o &#039;) a caracteres normales
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # Código comentado para versión de consola:
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """
        Verifica si la respuesta del usuario es correcta.
        Compara la respuesta del usuario con la respuesta correcta (sin distinguir mayúsculas/minúsculas).
        Incrementa la puntuación si la respuesta es correcta.
        
        Args:
            user_answer: Respuesta del usuario ("True" o "False")
        
        Returns:
            True si la respuesta es correcta, False en caso contrario
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

