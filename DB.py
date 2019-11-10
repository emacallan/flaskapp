from sqlalchemy import create_engine
from config import PGURL
import json
import re
from flask import abort

DB_URL = PGURL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
print(engine)


class AttributeExtender:
    def __init__(self, obj):
        try:
            self.__dict__ = obj
        except AttributeError:
            return None


class TransactionObj:
    def __init__(
        self, query_result=None, transaction_id=None, account_id=None, amount=None
    ):
        if query_result == None:
            self.person_id = account_id
            self.balance = amount
        else:
            self.person_id = str(query_result[0])
            self.balance = query_result[1]

    def __repr__(self):
        _repstring = (
            "{"
            + f""" "person_id":"{self.person_id}", "balance": {self.balance} """
            + "}"
        )
        return _repstring


class RequestHandler:
    def __init__(self, request):
        if request.json == None:
            abort(406, "Content-Type not json")

        self.payload = AttributeExtender(request.json)
        self.header = request.headers

    def __repr__(self):
        return f"""account_id:{self.payload.account_id}\namount:{self.payload.amount}"""


class db:
    def __init__(self, engine):
        self.engine = engine
        self.connection = engine.connect()

    def __contains__(self, obj):
        return obj in self.result

    def to_json(self):
        return json.dumps(json.loads(str(self.result)), indent=4)

    def get_balance(self, person_id_):
        balance_query = f"""
                with transactions as (
                    select id as transaction_id, person_id, amount as amount from Incomes where person_id = '{person_id_}'
                    UNION ALL
                    select id as transaction_id, person_id, -amount as amount from Expenses where person_id = '{person_id_}'
                )
                select person_id, sum(amount) as balance from transactions group by person_id;
            """

        self.result = TransactionObj(
            query_result=self.connection.execute(balance_query).fetchone()
        )

    def submit_amount(self, request):
        Table = "Incomes" if request.payload.amount >= 0 else "Expenses"
        submit_query = f"""
                insert into {Table} (id, person_id, amount) values(
                    '{request.header['Transaction-Id']}', '{request.payload.account_id}', '{request.payload.amount}'
                ); 
            """
        try:
            self.connection.execute(submit_query)
        except Exception as e:
            if "duplicate key" in re.findall("duplicate key", str(e)):
                abort(
                    409,
                    f"Attempted insertion of duplicate primary key into database.\n{e}",
                )
            else:
    §            abort(404, "Submission could not be performed")

    def person_exists(self, person_id_):
        query = f"select id, name from Persons where id='{person_id_}'"
        self.result = self.connection.execute(query).fetchone()
        try:
            return person_id_ in self.result[0]
        except TypeError:
            return False

    def transaction_exists(self, request):
        Table = 'Incomes' request.payload.amount >=0 else 'Expenses'
        query = f"select id from {Table} where id='{person_id_}'"
        self.result = self.connection.execute(query).fetchone()
        try:
            return person_id_ in self.result[0]
        except TypeError:
            return False

if __name__ == "__main__":
    pass
