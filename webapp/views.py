from datetime import datetime
from webapp import app,db
from flask import request,redirect,render_template
from .models import Submission,QuizAnswer

@app.route('/')
def index():
    return render_template('pages/index.html')



@app.route('/submit_data', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        # Submissionデータの抽出
        date = request.form['date']
        title = request.form['title']
        range_value = request.form['range']
        text = request.form['text']
        new_submission = Submission(date=datetime.strptime(date, '%Y-%m-%d'), title=title, range_value=range_value, text=text)
        db.session.add(new_submission)
        db.session.commit()
        
        # QuizAnswerデータの抽出と挿入
        quizzes = request.form.getlist('quiz[]')
        answers = request.form.getlist('answer[]')
        for quiz, answer in zip(quizzes, answers):
            new_quiz_answer = QuizAnswer(submission_id=new_submission.id, quiz=quiz, answer=answer)
            db.session.add(new_quiz_answer)
        
        db.session.commit()
        
        return redirect('/')  # 処理完了後のリダイレクト先
    


    
@app.route('/data-list', methods=['GET'])
def query_past_data():
    from .models import Submission, db,query_past_submissions, format_submission
    days = [1, 3, 7, 14, 28]  # 取得したい日数
    # 取得した提出物を格納するための空リストpast_submissionsを初期化しています。
    past_submissions = [] 

    # ここでは、指定した各日数に対してquery_past_submissions関数を呼び出し、その結果をresultsに格納します。それぞれの提出物（submission）に対して、format_submission関数を使用してフォーマットし、past_submissionsリストに追加しています。
    for day in days:
        results = query_past_submissions(day)
        for submission in results:
            formatted_submission = format_submission(submission)
            past_submissions.append(formatted_submission)

    print("Past submissions:", past_submissions)  # デバッグ用のプリント文

    return render_template('pages/learning-card.html',past_submissions=past_submissions)
