from flask import Flask, redirect, url_for, render_template, request, session, flash, wrappers, g
from functools import wraps

from users import users_blueprint
from gamehandler import gamehandler_blueprint
from quiz import quiz_blueprint
from pois import pois_blueprint
from hoops import hoops_blueprint
from giveaway import giveaway_blueprint


app = Flask(__name__)

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(gamehandler_blueprint, url_prefix='/gamehandeler')
app.register_blueprint(quiz_blueprint, url_prefix='/quiz')
app.register_blueprint(pois_blueprint, url_prefix='/pois')
app.register_blueprint(hoops_blueprint, url_prefix='/hoops')
app.register_blueprint(giveaway_blueprint, url_prefix='/giveaway')

app.secret_key = '<INSERT APP KEY HERE>'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)