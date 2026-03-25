import sqlite3

conn = sqlite3.connect('jogos.db')
cursor = conn.cursor()

# Criação da tabela jogos
cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Banco 'jogos.db' e tabela 'jogos' criados com sucesso!")
