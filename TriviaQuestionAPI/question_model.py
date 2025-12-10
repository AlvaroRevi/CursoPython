class Question:
    """
    Clase que representa una pregunta del quiz.
    Almacena el texto de la pregunta y su respuesta correcta.
    """

    def __init__(self, q_text, q_answer):
        """
        Inicializa una pregunta con su texto y respuesta.
        
        Args:
            q_text: Texto de la pregunta
            q_answer: Respuesta correcta (True o False)
        """
        self.text = q_text  # Texto de la pregunta
        self.answer = q_answer  # Respuesta correcta
