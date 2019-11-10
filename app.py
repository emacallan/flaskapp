from collections import namedtuple
from flask import Flask, jsonify, request, render_template, abort
import json, os, re
from sqlalchemy import create_engine
from config import PGURL
from DB import db, RequestHandler

DB_URL = PGURL
SQL_URI = "SQLALCHEMY_DATABASE_URI"
app = Flask(__name__)
app.config[SQL_URI] = DB_URL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)


@app.route("/balance/<person_id>", methods=["GET"])
def balance(person_id):
    db_ = db(engine)
    if db_.person_exists(person_id) == False:
        abort(404)
    db_.get_balance(person_id)
    db_.connection.close()
    return db_.to_json()


@app.route("/amount", methods=["GET", "POST"])
def insertion():
    req = RequestHandler(request)
    db_ = db(engine)

    try:
        person_exists = db_.person_exists(req.payload.account_id)
        transaction_exists = db_.transaction_exists(req)
        if type(req.payload.amount) == type(1) or type(req.payload.amount) == type(1.1):
            pass
        else:
            abort(
                406,
                f"'amount' must be either float or interger. type(amount):{type(req.payload.amount)}",
            )
            raise ValueError
    except AttributeError:
        abort(
            406,
            f"""missing information:(account_id|amount|Content-Type|Transaction-Id)""",
        )
    if not person_exists:
        abort(404, "User does not exists.")

    db_.submit_amount(req)
    db_.connection.close()
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=8080, passthrough_errors=True)
