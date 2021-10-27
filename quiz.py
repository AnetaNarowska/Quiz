from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
# number -numer pytania
class Question:
    def __init__(self,name,number) -> None:
        self.name = name
        self.number = number

questions = [Question('2+2=4?',1),Question('3+1=8?',2),
             Question('Czy Python ma klasy?',3)]
correct_answers = ['tak','nie','tak']


@app.route('/')
def index():
    return render_template('index.html',questions=questions)

@app.route('/result')
def result():
    answers = request.args
    score = 0
    for q,answer in answers.items():
        if correct_answers[int(q)-1]==answer:
            score = score+1
    return render_template('result.html',score=score)

if __name__=='__main__':
    app.run(debug=True)
    

    