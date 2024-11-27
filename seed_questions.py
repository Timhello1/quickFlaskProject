from app import create_app, db
from app.models import Question

questions = [
    Question(
        question_text="Which Python library is most commonly used for building neural networks?",
        option1="Scikit-learn",
        option2="TensorFlow",
        option3="Matplotlib",
        option4="Flask",
        correct_option="TensorFlow"
    ),
    Question(
        question_text="What is the primary purpose of the PyTorch library?",
        option1="Data visualization",
        option2="Web scraping",
        option3="Deep learning",
        option4="Natural Language Processing",
        correct_option="Deep learning"
    ),
    Question(
        question_text="Which Python library is designed for symbolic mathematics and algebra?",
        option1="SymPy",
        option2="NumPy",
        option3="Scikit-learn",
        option4="Pandas",
        correct_option="SymPy"
    ),
    Question(
        question_text="What is the function of the Keras library in AI development?",
        option1="Building and training machine learning models",
        option2="Handling database operations",
        option3="Creating 2D and 3D visualizations",
        option4="Web application development",
        correct_option="Building and training machine learning models"
    ),
    Question(
        question_text="Which Python library is most commonly used for natural language processing?",
        option1="NLTK",
        option2="OpenCV",
        option3="TensorFlow",
        option4="Matplotlib",
        correct_option="NLTK"
    ),
    Question(
        question_text="What does the 'fit' method in Scikit-learn do?",
        option1="Evaluates a model",
        option2="Trains a model on a dataset",
        option3="Prepares data for visualization",
        option4="Applies dimensionality reduction",
        correct_option="Trains a model on a dataset"
    ),
    Question(
        question_text="Which Python library is widely used for working with large datasets in AI?",
        option1="Pandas",
        option2="Scikit-learn",
        option3="Flask",
        option4="NumPy",
        correct_option="Pandas"
    ),
    Question(
        question_text="What is the primary goal of reinforcement learning in AI?",
        option1="To classify data into predefined categories",
        option2="To train agents to make decisions through rewards and penalties",
        option3="To preprocess data for analysis",
        option4="To visualize neural network layers",
        correct_option="To train agents to make decisions through rewards and penalties"
    ),
    Question(
        question_text="Which Python library provides pre-trained AI models and tools for transfer learning?",
        option1="Transformers by Hugging Face",
        option2="NumPy",
        option3="Scikit-learn",
        option4="Seaborn",
        correct_option="Transformers by Hugging Face"
    ),
    Question(
        question_text="What is the primary advantage of using Python in AI development?",
        option1="High execution speed",
        option2="Extensive library ecosystem",
        option3="Low memory usage",
        option4="Static typing",
        correct_option="Extensive library ecosystem"
    ),
    Question(
        question_text="Which Python library is designed for working with images and computer vision tasks?",
        option1="Matplotlib",
        option2="OpenCV",
        option3="Pandas",
        option4="Seaborn",
        correct_option="OpenCV"
    ),
    Question(
        question_text="What does a 'loss function' measure in AI model training?",
        option1="The accuracy of predictions",
        option2="The difference between predicted and actual values",
        option3="The speed of training",
        option4="The size of the dataset",
        correct_option="The difference between predicted and actual values"
    ),
    Question(
        question_text="Which Python library is commonly used for time-series forecasting in AI?",
        option1="Statsmodels",
        option2="Flask",
        option3="NumPy",
        option4="Matplotlib",
        correct_option="Statsmodels"
    ),
    Question(
        question_text="What does the term 'overfitting' refer to in AI?",
        option1="A model that performs well on training data but poorly on new data",
        option2="A model that underperforms on training data",
        option3="A model that uses too little data",
        option4="A model that generalizes well to new data",
        correct_option="A model that performs well on training data but poorly on new data"
    ),
    Question(
        question_text="Which Python library is known for distributed computing in machine learning?",
        option1="Dask",
        option2="Pandas",
        option3="Seaborn",
        option4="Statsmodels",
        correct_option="Dask"
    )
]

app = create_app()

with app.app_context():
    db.session.bulk_save_objects(questions)
    db.session.commit()
    print("Questions have been successfully added to the database!")
