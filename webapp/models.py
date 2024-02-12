from webapp import app,db
from datetime import datetime, timedelta
from .extensions import db

class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # 変更点
    title = db.Column(db.String(100))
    range_value = db.Column(db.String(50))
    text = db.Column(db.String(5000))
    quiz_answers = db.relationship('QuizAnswer', backref='submission', lazy=True)

class QuizAnswer(db.Model):
    __tablename__ = 'quiz_answers'
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    quiz = db.Column(db.String(500))
    answer = db.Column(db.String(500))




        

def query_past_submissions(days_ago):
    target_date = datetime.today() - timedelta(days=days_ago)
    target_date_str = target_date.strftime('%Y-%m-%d')
    results = Submission.query.filter(Submission.date == target_date_str).all()
    return results

def format_submission(submission):
    submission_data = {
        'id': submission.id,
        'date': submission.date,
        'title': submission.title,
        'text': submission.text,
        'quizzes': [
            {'quiz': qa.quiz, 'answer': qa.answer} 
            for qa in submission.quiz_answers if qa is not None
        ]
    }
    print([qa for qa in submission.quiz_answers])
    return submission_data


