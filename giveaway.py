from flask import Blueprint, request, jsonify
from functools import wraps
import requests

from database import users



giveaway_blueprint = Blueprint('giveaway_blueprint', __name__)


@giveaway_blueprint.route('/giveaway/redeem', methods=['POST'])
def redeem_giveaway():
    data = request.get_json()

    redeem_request = data['redeem_request']
    seat = data['seat']

    user_query = users.find_one({'Seat': seat})
    num_tickets = user_query['Tickets']


    redeemables = ['Raffle Entry', 'Song Request', 'Merch']

    if redeem_request in redeemables:
        if num_tickets >= 1:
            users.update_one({'Seat': seat}, {'$inc': {'Tickets': -1}})

            if redeem_request == 'Raffle Entry':
                users.update_one({'Seat': seat}, {'$inc': {'Raffle': 1}})
                return jsonify({'redeem_request': 'Raffle Entry', 'success': True})
            elif redeem_request == 'Song Request':
                song = data['song']
                r = requests.post('http://localhost:5000/song/request', json={'song': song})
            elif redeem_request == 'Merch':
                r = requests.post('http://localhost:5000/merch/request', json={'merch': merch, 'seat': seat})
            
            
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Not enough tickets'})