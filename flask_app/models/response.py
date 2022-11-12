from flask import session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.topic import Topic

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
        query = 'INSERT INTO responses (choice, user_id, topic_id) VALUES (%(choice)s, %(user_id)s, %(topic_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_vote(response):
        query = 'SELECT * FROM responses LEFT JOIN topics ON responses.topic_id = topics.id WHERE topics.id = %(id)s;'
        results = connectToMySQL(Response.db).query_db(query, response)
        is_valid = True
        for row in results:
            if row.user_id == session['user_id']:
                flash('Cannot vote twice')
                is_valid = False
        return is_valid