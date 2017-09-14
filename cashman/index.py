# coding=utf-8

from flask import Flask, jsonify

app = Flask(__name__)

users = [{
    "name": "Bruno",
    "age": 33
}, {
    "name": "José",
    "age": 35
}]


@app.route('/users/')
def getUsers():
    return jsonify(users)
