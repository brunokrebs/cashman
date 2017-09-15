# coding=utf-8

from flask import Flask, jsonify, request
from model.expense import Expense, ExpenseSchema

app = Flask(__name__)

expenses = [Expense("pizza", 50), Expense("Rock Concert", 100)]


@app.route('/expenses/')
def getExpenses():
    schema = ExpenseSchema(many=True)
    result = schema.dump(expenses)
    return jsonify(result.data)
