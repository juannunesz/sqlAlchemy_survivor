from infra.configs.connection import DBConnectionHandler
from app.entities.filmes import Filmes

class FilmesRepository:
    
    def select(self):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Filmes).all()
            except Exception as exception:
                raise exception

    def insert(self, titulo: str, genero: str, ano: int): 
        with DBConnectionHandler() as db:
            try:
                db.session.add(Filmes(titulo=titulo, genero=genero, ano=ano))
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, titulo: str, data_update: dict): 
        with DBConnectionHandler() as db:
            try: 
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update(data_update)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo: str): 
        with DBConnectionHandler() as db:
            try: 
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception