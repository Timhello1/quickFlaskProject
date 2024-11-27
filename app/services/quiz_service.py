from app.models import Question, UserScore
from app import db

def get_all_questions():
    """Pobiera wszystkie pytania z bazy danych."""
    return Question.query.all()

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
