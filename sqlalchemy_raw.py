from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

#config
engine = create_engine("mysql+pymysql://root:password@localhost/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
 
# Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [(titulo={self.titulo}, ano={self.ano})]"

# Insert
data_insert = Filmes(titulo="Interestelar", genero="Drama", ano=2013)
session.add(data_insert)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.titulo == "Dracula").delete()
session.commit()

# Update 
session.query(Filmes).filter(Filmes.titulo == "Dracula").update({ "ano": 2000 })
session.commit()

# Select 
data = session.query(Filmes).all()
print(data)

session.close()
