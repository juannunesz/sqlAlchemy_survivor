from infra.configs.connection import DBConnectionHandler
from app.entities.atores import Atores
from app.entities.filmes import Filmes

class AtoresRepository:
    
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session\
                    .query(Atores, Filmes)\
                    .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                    .with_entities(
                        Atores.nome,
                        Filmes.genero,
                        Filmes.titulo
                    )\
                    .all()
                return data
            except Exception as exception:
                raise exception
            
    def insert(self, nome: str): 
        with DBConnectionHandler() as db:
            try:
                db.session.add(Atores(nome=nome))
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id: int, data_update: dict): 
        with DBConnectionHandler() as db:
            try:
                db.session.query(Atores).filter(Atores.id == id).update(data_update)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id: int): 
        with DBConnectionHandler() as db:
            try:
                db.session.query(Atores).filter(Atores.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
