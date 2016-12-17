from sqlalchemy import create_engine, text
from rx import Observable

engine = create_engine('sqlite:///C:\\Users\\thoma\\Dropbox\\rexon_metals.db')
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return Observable.from_(conn.execute(stmt))


get_all_customers().subscribe(lambda r: print(r))
