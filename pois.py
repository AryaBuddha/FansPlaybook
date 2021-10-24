from flask import Blueprint, request, jsonify
from functools import wraps

from users import add_ticket
from database import POIs, users

from users import add_ticket


pois_blueprint = Blueprint('pois_blueprint', __name__)


@pois_blueprint.route('/verifyPOI', methods=['POST'])
def verify_poi():
    data = request.get_json()
    poi_id = data['poi_id']

    
    POIs_doc = POIs.find_one()
    POIs_list = POIs_doc['POIs']

    user_doc = users.find_one({'Seat': data['seat']})
    user_POIs = user_doc['POIs']

    if poid_id in user_POIs:
        return jsonify({'message': 'You have already scanned this POI', 'status': 'fail'})
    elif poi_id not in user_POIs and poi_id in POIs_list:
        return jsonify({'message': 'Claimed a new POI', 'status': 'success'})
        users.update_one({'Seat': data['seat']}, {'$push': {'POIs': poi_id}})
        add_ticket(data['seat'])
    



    
