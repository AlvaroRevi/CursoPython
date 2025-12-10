# Importación de las clases y datos necesarios para el juego
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Crear una lista vacía para almacenar todas las preguntas del quiz
question_bank = []

# Convertir los datos de la API en objetos Question y añadirlos al banco de preguntas
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Crear una instancia de QuizBrain con el banco de preguntas
quiz = QuizBrain(question_bank)

# Crear e iniciar la interfaz gráfica del quiz
quiz_ui = QuizInterface(quiz)


