# coding=utf-8

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users/')
def users():
    bruno = {
        "name": "Bruno",
        "age": 33
    }
    jose = {
        "name": "José",
         "age": 35
    }
    all_users = [ bruno, jose ]
    return jsonify(all_users)
