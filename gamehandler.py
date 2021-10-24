from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
import time

from database import schedule


gamehandler_blueprint = Blueprint('gamehandler_blueprint', __name__)

"""
Challonge data could be used here to dynamically identify breaks and halftimes. That way no manual input of timesatamps is needed.
"""


@gamehandler_blueprint.route('/nextGame', methods=['GET'])
def next_game():
    """
    Returns the next game in the schedule.
    """
    current_schedule = schedule.find_one(schedule.find_one())

    current = time.time()

    game_list = list(current_schedule['gameSchedule'].keys())
    stamp_list = list(current_schedule['gameSchedule'].values())

    next_game = ''
    for stamp in stamp_list:
        if current < stamp:
            next_game = game_list[stamp_list.index(stamp)]
            break

    return jsonify({'nextGame': next_game}), 200



@gamehandler_blueprint.route('/currentGame', methods=['GET'])
def current_game():
    """
    Returns the current game in the schedule.
    """
    current_schedule = schedule.find_one(schedule.find_one())

    current = time.time()

    game_list = list(current_schedule['gameSchedule'].keys())
    stamp_list = list(current_schedule['gameSchedule'].values())

    current_game = ''
    for stamp in stamp_list:
        if current > stamp:
            current_game = game_list[stamp_list.index(stamp)]
            

    return jsonify({'currentGame': current_game}), 200

        



def get_current_game():
    """
    Returns the current game in the schedule.
    """
    current_schedule = schedule.find_one(schedule.find_one())

    current = time.time()

    game_list = list(current_schedule['gameSchedule'].keys())
    stamp_list = list(current_schedule['gameSchedule'].values())

    current_game = ''
    for stamp in stamp_list:
        if current > stamp:
            current_game = game_list[stamp_list.index(stamp)]
            

    return current_game
     

        

