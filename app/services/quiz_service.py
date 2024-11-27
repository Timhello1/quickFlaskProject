from app.models import Question, UserScore
from app import db
import random

def get_all_questions(number_of_questions=3):
    """Pobiera wszystkie pytania z bazy danych."""
    questions = Question.query.all()
    return random.sample(questions, min(number_of_questions, len(questions)))

def save_user_score(username, score):
    """Zapisuje wynik użytkownika."""
    user_score = UserScore(username=username, score=score)
    db.session.add(user_score)
    db.session.commit()

def calculate_score(user_answers):
    """Oblicza wynik quizu na podstawie odpowiedzi użytkownika."""
    questions = get_all_questions()
    score = 0
    for question in questions:
        if user_answers.get(f"question{question.id}") == question.correct_option:
            score += 1
    return score
