from pymongo import MongoClient



mongo_url = 'Database ID Login Here'

cluster = MongoClient(mongo_url)

users = cluster['Users']
sections = cluster['Sections']
POIs = cluster['POIs']
questions = cluster['Questions']
schedule = cluster['Schedule']
hoops = cluster['Hoops']
