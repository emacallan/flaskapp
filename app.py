from collections import namedtuple
from flask import Flask, jsonify, request, render_template, abort 
import json, os 
from flask_sqlalchemy  import SQLAlchemy as sql
from sqlalchemy import create_engine
from config import PGURL
from DB import db,  RequestHandler

DB_URL = PGURL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
# db = sql(app)






    
@app.route("/balance/<id_>", methods=["GET"])
def balance(id_):
    db_ = db(engine)
    if  db_.person_exists(id_) == False:
        abort(404)
    db_.get_balance(id_)
    return db_.to_json()


@app.route('/amount', methods=['GET','POST'])
def insertion():
    req = RequestHandler(request)
    db_ = db(engine)
    exists = db_.person_exists(req.payload.account_id)
    if not exists: 
        # insert new user? 
        pass 
    if type(req.payload.amount) == type(1) or type(req.payload.amount) == type(1.1):
        pass
    else:
        raise ValueError
    db_.submit_amount(req)
        

    return ''
    # except Exception as e: print(e); abort(403)
    




if __name__ == "__main__":

    # os.sytem("export FLASK_APP=app.py && export FLASK_RUN_PORT=8080 && python3 -m flask run")
    app.run(debug=True, port = 8080, passthrough_errors=True)

