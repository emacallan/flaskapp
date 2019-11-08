from collections import namedtuple
from flask import Flask, jsonify, request, render_template, abort 
import json 
from flask_sqlalchemy  import SQLAlchemy as sql
from sqlalchemy import create_engine
from config import PGURL
from DB import db, Persons, Transaction, RequestHandler

DB_URL = PGURL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
# db = sql(app)






def person_exists(id_):

    person = Persons(engine)
    person.query(f"select id, name from Persons where id='{id_}'")
    print(person.result)
    if id_ not in person:
        abort(404)

    
@app.route("/balance/<id_>", methods=["GET"])
def balance(id_):
    person_exists = Persons
    person_balance = Transaction(engine)
    person_balance.query(f"""
                        with transactions as (
                            select id as transaction_id, person_id, amount as amount from Incomes where person_id = '{id_}'
                            UNION ALL
                            select id as transaction_id, person_id, -amount as amount from Expenses where person_id = '{id_}'
                        )
                        select person_id, sum(amount) as balance from transactions group by person_id;
    """)

    return json.dumps(person_balance.to_json())


@app.route('/amount', methods=['GET','POST'])
def insertion():
    req = RequestHandler(request)
    person_exists(req.payload.account_id)

    if type(req.payload.amount) == type(1) or type(req.payload.amount) == type(1.1):
        print(type(req.payload.amount), type(1))
    else:
        raise ValueError
    Table = 'Incomes' if req.payload.amount >= 0 else 'Expense'
    trans = Transaction(engine) 
    try:

        trans.insert(f"""
                insert into {Table} (id, person_id, amount) values(
                    '{req.header['Transaction-Id']}', '{req.payload.account_id}', '{req.payload.amount}'
                ); 
        """)
        

        return ''
    except Exception as e: print(e); abort(403)
    




if __name__ == "__main__":
    app.run(debug=True)

