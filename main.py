from flask import Flask, request, render_template, redirect, url_for

import BooleanQAModel
# import NumberModel
# import TextModel

app = Flask(__name__)

booleanQAModel = BooleanQAModel.BooleanQAModel('./resources/models/BooleanQAModel.pth')
# numberModel = NumberModel()
# textModel = TextModel()

data = {
    'context': '',
    'question': '',
    'answer': 'Answer will appear here...'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    context = request.form.get("context")
    question = request.form.get("question")
    data['context'] = context
    data['question'] = question
    data['answer'] = booleanQAModel.predict(context, question)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
