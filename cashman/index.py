# coding=utf-8

from flask import Flask, jsonify, request
from model.expense import Expense, ExpenseSchema
from model.income import Income, IncomeSchema

app = Flask(__name__)

expenses = [Expense("pizza", 50), Expense("Rock Concert", 100)]
incomes = [Income("Salary", 5000), Income("Dividends", 200)]


@app.route('/expenses/')
def get_expenses():
    schema = ExpenseSchema(many=True)
    result = schema.dump(expenses)
    return jsonify(result.data)


@app.route('/expenses/', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    expenses.append(expense.data)
    return '', 204


@app.route('/incomes/')
def get_incomes():
    schema = IncomeSchema(many=True)
    result = schema.dump(incomes)
    return jsonify(result.data)


@app.route('/incomes/', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    incomes.append(income.data)
    return '', 204
