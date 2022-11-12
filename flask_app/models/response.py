from flask import session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.topics import Topic

class Response:
    db = "hot_topic"
    def __init__(self,data):
        self.id = data['id']
        self.choice = data['choice']
        self.user_id = session['user_id']
        self.topic_id = data['topic_id']

#Adds the voting choice to the responses table
    @classmethod
    def submit_choice(cls,data):
        query = 'INSERT INTO responses (choice, user_id, topic_id, created_at, updated_at) VALUES (%(choice)s, %(user_id)s, %(topic_id)s, NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)