from collections import namedtuple
from flask import Flask, jsonify, request
import json 
from flask_sqlalchemy  import SQLAlchemy as sql
from sqlalchemy import create_engine
from config import POSTGRES_DB, POSTGRES_URL, POSTGRES_PW, POSTGRES_USER
from DB import db, Persons, Balance, RequestHandler

DB_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
# db = sql(app)






@app.route('/')
def hello_world():
    return 'Hello, World!\nBye world!'


@app.route('/tryme', methods = ['GET'])
def persons():

    people = Persons(engine)
    people.query("select id, name from Persons where name = 'Stephen Ogden';")
    print(people.to_json())
    return json.dumps(people.to_json())
    
@app.route("/balance/<id_>")
def balance(id_):
    person_balance = Balance(engine)
    person_balance.query(f"""
                        with transactions as (
                            select person_id, amount as amount from Incomes where person_id = '{id_}'
                            UNION ALL
                            select person_id, -amount as amount from Expenses where person_id = '{id_}'
                        )
                        select person_id, sum(amount) as balance from transactions group by person_id;
    """)

    return json.dumps(person_balance.to_json())

@app.route("/amount/<id_>", methods=['GET', 'POST'])
def insert_amount(id_):
    payload = request.json
    print(request.headers)
    transaction = Balance(engine)
    transaction.insert(**payload)
    req = RequestHandler(request)
    q = f"""
            insert into Expenses (transaction_id, person_id, amount) 
                values ('{request.headers['Transaction-Id']}', '{transaction.result.person_id}', {transaction.result.balance})
    """
    req.query = q 
    per = Persons(engine)
    per.query(f"select id, name from Persons where id = '{req.payload.account_id}'")
    print(req.payload.account_id in per.result, req.payload.account_id,per.result)
    return per.to_json()
    
    exit()
    # person_transaction = Balance(engine)
    # person_transaction.query(f"""
                        
    
    # """)


if __name__ == "__main__":
    app.run(debug=True)

