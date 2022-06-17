CREATE DATABASE IF NOT EXISTS cinema;

USE cinema:

CREATE TABLE IF NOT EXISTS filmes (
    id BIGINT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL, 
    genero VARCHAR(30) NOT NULL,
    ano INT NOT NULL, 
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS atores (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    id_filme BIGINT NOT NULL,
    PRIMARY KEY(id),
    FOREGIN KEY (titulo_filme) REFERENCES filmes(id)
);

INSERT INTO atores (nome, titulo_filme)
VALUE ("Tom Hanks", "Forest Gump")

INSERT INTO filmes (titulo, genero, ano)
VALUE ("Forest Gump", "Dreama", 1994);