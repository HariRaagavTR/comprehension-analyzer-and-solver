from flask import Flask, request, render_template, redirect, url_for

from QuestionType import QuestionType
from BooleanQAModel import BooleanQAModel
# import NumberModel
# import TextModel

data = {
    'context': '',
    'question': '',
    'answer': 'Answer will appear here...'
}

questionType = QuestionType()
booleanQAModel = BooleanQAModel('./resources/models/BooleanQAModel.pth')
# numberModel = NumberModel()
# textModel = TextModel()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    context = request.form.get("context")
    question = request.form.get("question")

    qType = questionType.predict(question)
    if qType == 'boolean':
        answer = booleanQAModel.predict(context, question)
    elif qType == 'numerical':
        answer = ''
    else:
        answer = ''
    
    data['context'] = context
    data['question'] = question
    data['answer'] = answer
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
