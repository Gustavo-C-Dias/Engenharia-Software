import sqlite3

conn = sqlite3.connect('user.bd')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE usuario (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf  VARCHAR(11) NOT NULL,
        senha VARCHAR (16) NOT NULL
);""")

cursor.execute("""
CREATE TABLE valores (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    peso FLOAT NOT NULL,
    altura FLOAT NOT NULL,
    imc FLOAT NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);""")

conn.close()