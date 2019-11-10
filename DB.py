from sqlalchemy import create_engine
import json 
from config import PGURL
DB_URL = PGURL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
print(engine)
class foo:

    def __init__(self, obj): self.__dict__ = obj
        
class TransactionObj:

    def __init__(self, query_result = None, transaction_id = None, account_id = None, amount = None):
        if query_result == None:
            self.person_id = account_id
            self.balance = amount
        else:
            print(query_result)
            # assert len(query_result) == 1 or query_result == None
            # self.transaction_id = str(query_result[0][0])
            self.person_id = str(query_result[0])
            self.balance = query_result[1]

    def __repr__(self):

        return "{"+f""" "person_id":"{self.person_id}", "balance": {self.balance} """+"}"

class RequestHandler:

    def __init__(self,request):
        self.payload = foo(request.json) 
        self.header = request.headers

    # def __repr__(self):

    #     return f"{self.request}"
    def __repr__(self):
        return f"""account_id:{self.payload.account_id}\namount:{self.payload.amount}"""


class db:

    def __init__(self, engine):
        self.engine = engine
        self.connection = engine.connect()

    def __contains__(self, obj):    
        return obj in self.result

    def get_balance(self, id_):
        q = f"""
                with transactions as (
                    select id as transaction_id, person_id, amount as amount from Incomes where person_id = '{id_}'
                    UNION ALL
                    select id as transaction_id, person_id, -amount as amount from Expenses where person_id = '{id_}'
                )
                select person_id, sum(amount) as balance from transactions group by person_id;
            """
        self.result = TransactionObj(self.connection.execute(q).fetchone())
        print('\t', str(self.result))
        

    def submit_amount(self, req): 
        Table = 'Incomes' if req.payload.amount >= 0 else 'Expenses'
        q = f"""
                insert into {Table} (id, person_id, amount) values(
                    '{req.header['Transaction-Id']}', '{req.payload.account_id}', '{req.payload.amount}'
                ); 
            """
        self.connection.execute(q)

    def person_exists(self, id_):
        q = f"select id, name from Persons where id='{id_}'"
        self.result = self.connection.execute(q).fetchone()
        print(self.result)
        return id_ in self.result[0]

    # def create_account(self, req):
    #     q = f"inset into Persons (id, name) values('{req.payload.account_id}', 'foo')" 
    #     self
    def to_json(self):

        return json.dumps(json.loads(str(self.result)), indent= 4)

