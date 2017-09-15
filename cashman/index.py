# coding=utf-8

from flask import Flask, jsonify, request
from model.expense import Expense, ExpenseSchema

app = Flask(__name__)

expenses = [Expense("pizza", 50), Expense("Rock Concert", 100)]


@app.route('/expenses/')
def get_expenses():
    schema = ExpenseSchema(many=True)
    result = schema.dump(expenses)
    return jsonify(result.data)


@app.route('/expenses/', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    expenses.append(expense.data)
    return ('', 204)
