from sqlalchemy import create_engine
import json 
from config import PGURL
DB_URL = PGURL
engine = create_engine(DB_URL, convert_unicode=True, echo=False)
print(engine)
class foo:

    def __init__(self, obj): self.__dict__ = obj
        
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
        

class PersonsObj: 

    def __init__(self, query_result):
        self.id = str(query_result[0])
        self.name = str(query_result[1])

    def __repr__(self):

        return "{"+f""" "name":"{self.name}", "id": "{self.id}" """+"}"

class Persons(db): 

    def __init__(self, engine):
        super().__init__(engine)

    def query(self, q):
        results = self.connection.execute(q).fetchall()
        if len(results) == 1: 
            self.result = str(PersonsObj(results[0]))
        else:
            self.result = [PersonsObj(result) for result in self.connection.execute(q).fetchall()]

    def to_json(self):

        return json.dumps(json.loads(str(self.result)), indent= 4)


    def __contains__(self,obj):

        return obj in self.result

class TransactionObj:

    def __init__(self, query_result = None, transaction_id = None, account_id = None, amount = None):
        if query_result == None:
            self.person_id = account_id
            self.balance = amount
        else:
            print(query_result)
            # assert len(query_result) == 1 or query_result == None
            # self.transaction_id = str(query_result[0][0])
            self.person_id = str(query_result[0][0])
            self.balance = query_result[0][1]
    
    def __repr__(self):

        return "{"+f""" "person_id":"{self.person_id}", "balance": {self.balance} """+"}"

class Transaction(db):

    def __init__(self, engine):
        super().__init__(engine)

    def query(self,q):
        self.result = TransactionObj(query_result = self.connection.execute(q).fetchall())
    
    def insert(self,q):
        self.connection.execute(q)

        # self.result = TransactionObj(**kwargs) 

    def to_json(self):

        return json.dumps(json.loads(str(self.result)), indent= 4)

    def __str__(self):

        return f"{self.result}"

