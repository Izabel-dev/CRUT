# Game Inventory API - CRUD Completo com CURL

Este projeto é uma **API REST para gerenciar um inventário de jogos** usando **Python, Flask e SQLite**.  
O foco deste README é mostrar **como usar todas as funcionalidades via linha de comando `curl`**, sem precisar de interface gráfica.

---

## 🔹 Tecnologias

- Python 3.x  
- Flask  
- SQLite  

---

## 🔹 Estrutura do projeto

---

## 🔹 Passo 1: Criar o banco de dados

No CMD, execute:

```bat
python init_db.py

Passo 2: Rodar a API

venv\Scripts\activate.bat

python app.py

http://127.0.0.1:5000

Rotas e exemplos de uso com CURL
1 .Listar todos os jogos

curl http://127.0.0.1:5000/jogos

[
  {"id":1,"titulo":"Cyberpunk 2077","plataforma":"PC","preco":99.9,"estoque":7},
  {"id":2,"titulo":"GTA V","plataforma":"PC","preco":79.9,"estoque":15}

2. Listar um jogo específico

curl http://127.0.0.1:5000/jogos/1

{"id":1,"titulo":"Cyberpunk 2077","plataforma":"PC","preco":99.9,"estoque":7}

Criar um novo jogo (POST)

curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\":\"Zelda: Breath of the Wild\",\"plataforma\":\"Nintendo Switch\",\"preco\":299.9,\"estoque\":5}"

{"mensagem": "Jogo criado com sucesso!"}

Atualizar um jogo (PUT)

curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\":\"Cyberpunk 2077\",\"plataforma\":\"PC\",\"preco\":79.9,\"estoque\":10}"

{"mensagem": "Jogo atualizado com sucesso!"}

Deletar um jogo (DELETE)

curl -X DELETE http://127.0.0.1:5000/jogos/2

{"mensagem": "Jogo 'GTA V' removido!"}

{"erro": "Jogo não encontrado"}

Aplicar desconto em todos os livros ou jogos de uma plataforma

@app.route('/desconto/<string:plataforma>/<int:percent>', methods=['PUT'])
def aplicar_desconto(plataforma, percent):
    executar_query(
        "UPDATE jogos SET preco = preco * ? WHERE plataforma = ?",
        (1 - percent/100, plataforma),
        commit=True
    )
    return jsonify({"mensagem": f"Desconto de {percent}% aplicado em todos os {plataforma}!"}), 200

curl -X PUT http://127.0.0.1:5000/desconto/Livro/10

{"mensagem": "Desconto de 10% aplicado em todos os Livro!"}

]
