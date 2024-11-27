from flask import Blueprint, render_template, request, session
from app.services.quiz_service import get_all_questions, save_user_score, calculate_score

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/')
def home():
    questions = get_all_questions()
    best_score = session.get('best_score', 0)
    return render_template('quiz_template.html', questions=questions, best_score=best_score)

@quiz_bp.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form
    score = calculate_score(user_answers)

    # Zapisz najlepszy wynik w sesji
    if score > session.get('best_score', 0):
        session['best_score'] = score

    # Zapisz wynik użytkownika w bazie danych
    save_user_score(username="Anonymous", score=score)

    return render_template('result.html', score=score, best_score=session['best_score'], total=len(get_all_questions()))
