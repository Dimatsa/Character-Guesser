from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/guess/', methods=['GET'])
def guess():
    answers = request.args.get('1. Does your character have yellow skin')
    answers2 = request.args.get('2. Does your character live in the future')
    answers3 = request.args.get('3. Is your character an ape')
    return jsonify(answers,answers2,answers3)


@app.route('/questions/', methods=['GET'])
def questions():
    answers = request.args.get('answers')
    questions = (
        'Is your character real?',
        'Is your character male?',
        'Does your character have a bad haircut?'
    )
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)