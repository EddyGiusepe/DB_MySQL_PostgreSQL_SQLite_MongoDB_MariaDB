from urllib import response
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:colocar_a_minha_EDDY@localhost:3306/cinema')
conn = engine.connect()
response = conn.execute('SELECT * FROM filmes;')
#response = engine.execute('SELECT * FROM filmes;')

for row in response:
    print(row)
    print(row.titulo)
    