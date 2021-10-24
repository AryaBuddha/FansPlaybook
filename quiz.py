from flask import Blueprint, request, jsonify
from functools import wraps

from database import questions

from gamehandler import get_current_game
from users import add_ticket


quiz_blueprint = Blueprint('quiz_blueprint', __name__)

def checkGame(f):
    @wraps(f)
    def wrapFunc():
        if get_current_game() is not 'Quiz':
            return jsonify({'error': 'Not in quiz mode'})
    return wrapFunc



@quiz_blueprint.route('/getQuestions', methods=['GET'])
@checkGame
def get_questions():
    question_doc = questions.find_one({'Type': 'Questions'})


    return jsonify({'questions': question_doc['Questions']})


@quiz_blueprint.route('/checkAnswers', methods=['GET'])
@checkGame
def check_answers():
    data = request.get_json()
    user_answers = data['answers']

    answer_doc = questions.find_one({'Type': 'Answers'})
    answers = answer_doc['Answers']

    correct_answers = 0

    for i in range(len(user_answers)):
        if user_answers[i] == answers[i]:
            correct_answers += 1

    if(correct_answers > (0.8 * user_answers)):
        return jsonify({'status': 'Winner'})
        add_ticket(data['seat'])
    else:
        return jsonify({'status': 'Loser'})
