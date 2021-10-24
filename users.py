from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId

from database import users
from database import sections


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        try:
            user = users.find_one({'Seat': data['seat']})
            tmp = user['NumTickets']

            return jsonify({'status': 'error', 'message': 'Seat already taken'}), 400
        except:
            user_template = {
                'Seat': data['seat'],
                'NumTickets': 0,
                'POIs': [],
                'GameResults': {},
                'Raffle': 0
            }

            users.insert_one(user_template)
            return jsonify({'status': 'success', 'message': 'User registered!'}), 200


def add_ticket(seat):
    user = users.find_one({'Seat': seat})
    tmp = user['NumTickets']
    users.update_one({'Seat': seat}, {'$set': {'NumTickets': tmp + 1}})

    section = seat[0]
    section_tickets = sections.find_one({'Section': section})['Tickets']
    sections.update_one({'Section': section}, {'$set': {'NumTickets': section_tickets + 1}})


def remove_ticket(seat):
    user = users.find_one({'Seat': seat})
    tmp = user['NumTickets']
    users.update_one({'Seat': seat}, {'$set': {'NumTickets': tmp - 1}})

