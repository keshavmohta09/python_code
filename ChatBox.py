import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:q1w2e3r4@localhost:3306/test1')
print("For refresh press [Enter], For quit type 'exit' or Type a message")
sender = input('Enter your name : ')

def send_message(message):
    try:
        qry = f"INSERT INTO ChatData VALUES ('{sender}','{message}');"
        pd.read_sql_query(qry,engine)
    except:
        refresh()

def refresh():
    qry = "select * from ChatData;"
    df = pd.read_sql_query(qry,engine)
    print()
    print(df)

while True:
    message = input('\nType a message....\n')
    if message=='exit':
        qry = "truncate table ChatData;"
        try:
            pd.read_sql_query(qry,engine)
        except:
            pass
        exit()
    elif message=='':
        refresh()
    else:
        send_message(message)