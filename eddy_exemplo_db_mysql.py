'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
''' 
print("Primeira forma de se conectar com MySQL:")
# from sqlalchemy import create_engine
# import pymysql
# import pandas as pd

# conexao = create_engine('mysql+pymysql://root:Diosymispadres1#@localhost:3306/cinema')
# df = pd.read_sql('SELECT * FROM filmes', con=conexao)
# print(df.head())


print("Segunda forma de se conectar com MySQL:")
import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('mysql+pymysql://root:ADICIONAR_SENHA_EDDY@localhost:3306/cinema')
qry = 'SELECT * FROM filmes;'
df = pd.read_sql_query(qry, engine)
print(df.head(20))


