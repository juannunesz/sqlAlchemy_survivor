from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler: 

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:password@localhost/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        
    def __create_database_engine(self): 
        return create_engine(self.__connection_string)

    def get_engine(self): 
        return self.__engine 
