from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cashman.model.base import Base
from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema

app = Flask(__name__)
engine = create_engine('postgresql://dbuser:dbpassword@localhost:5432/cashman')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


@app.route('/incomes')
def get_incomes():
    session = Session()
    schema = IncomeSchema(many=True)
    incomes = session.query(Income)

    return jsonify(
        schema.dump(incomes).data
    )


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())

    session = Session()
    session.add(income.data)
    session.commit()

    return "", 204


@app.route('/expenses')
def get_expenses():
    session = Session()
    schema = ExpenseSchema(many=True)
    expenses = session.query(Expense)

    return jsonify(
        schema.dump(expenses).data
    )


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())

    session = Session()
    session.add(expense.data)
    session.commit()

    return "", 204


if __name__ == "__main__":
    app.run()
