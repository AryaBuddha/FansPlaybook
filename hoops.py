from flask import Blueprint, request, jsonify
from functools import wraps
import random

from database import sections, hoops

from gamehandler import get_current_game
from users import add_ticket


hoops_blueprint = Blueprint('hoops_blueprint', __name__)

def checkGame(f):
    @wraps(f)
    def wrapFunc():
        if get_current_game() is not 'Hoops':
            return jsonify({'error': 'Not in hoops mode'})
    return wrapFunc


@hoops_blueprint.route('/startHoops', methods=['GET'])
@checkGame
def start_hoops():
    data = request.get_json()
    try:
        matchup = hoops.find_one({'opponent_section', data['seat']})
        opponent_section = matchup['user_seat']

        return jsonify({'opponent': opponent_section})

    except:
        user_seat = data['seat']

        upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        upper_alphabet.remove(user_seat[0])

        opponent_section = random.choice(upper_alphabet)
        hoops.insert_one({'user_seat': user_seat[0], 'opponent_section': opponent_section})
        
        return jsonify({'opponent': opponent_section})




@hoops_blueprint.route('/checkHoops', methods=['GET'])
@checkGame
def check_hoops():
    data = request.get_json()
    try:
        matchup = hoops.find_one({'user_seat', data['seat']})

        hoops.update_one({'user_seat': data['seat']}, {'$set': {'user_score': data['score']}})

        return jsonify({'status': 'success'})

    except:
        matchup = hoops.find_one({'opponent_section', data['seat']})

        hoops.update_one({'opponent_section': data['seat']}, {'$set': {'opponent_score': data['score']}})

        return jsonify({'status': 'success'})



@hoops_blueprint.route('/endHoops', methods=['GET'])
@checkGame
def end_hoops():
    data = request.get_json()
    try:
        matchup = hoops.find_one({'user_seat', data['seat']})

        user_score = data['score']
        opponent_score = matchup['opponent_score']

        if user_score > opponent_score:
            add_ticket(matchup['user_seat'])
            return jsonify({'message': 'You won!'})
        elif user_score < opponent_score:
            add_ticket(matchup['opponent_section'])
            return jsonify({'message': 'You lost!'})

    except:
        matchup = hoops.find_one({'opponent_section', data['seat']})

        user_score = matchup['user_score']
        opponent_score = data['score']
        
        if user_score > opponent_score:
            return jsonify({'message': 'You list!'})
        elif user_score < opponent_score:
            add_ticket(matchup['user_seat'])
            return jsonify({'message': 'You won!'})
            