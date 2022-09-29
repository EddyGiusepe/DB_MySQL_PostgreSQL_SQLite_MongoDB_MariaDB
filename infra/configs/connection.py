from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:Diosymispadres1#@localhost:3306/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None # É pública porque não tem underline


    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine         

    def get_engine(self):
        return self.__engine

    # Sempre que eu entrar eu crio uma sessão
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self 

    # E sempre que sair eu vou feccho a minha sessão 
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  






