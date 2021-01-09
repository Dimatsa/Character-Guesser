from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/guess/', methods=['GET'])
def guess():
    print(request.args)
    return jsonify(request.args)

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