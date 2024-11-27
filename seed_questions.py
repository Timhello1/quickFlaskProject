from app import create_app, db
from app.models import Question

questions = [
    Question(
        question_text="What is the main use of Python in AI?",
        option1="Data analysis",
        option2="Web design",
        option3="Hardware design",
        option4="Game development",
        correct_option="Data analysis"
    ),
    Question(
        question_text="Which library is commonly used for computer vision in Python?",
        option1="NumPy",
        option2="Pandas",
        option3="OpenCV",
        option4="Scikit-learn",
        correct_option="OpenCV"
    ),
    Question(
        question_text="What does NLP stand for?",
        option1="Natural Learning Process",
        option2="Natural Language Processing",
        option3="Neural Learning Process",
        option4="None of the above",
        correct_option="Natural Language Processing"
    )
]

app = create_app()

with app.app_context():
    db.session.bulk_save_objects(questions)
    db.session.commit()
    print("Questions have been successfully added to the database!")
