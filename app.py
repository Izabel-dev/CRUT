from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Função auxiliar para executar queries
def executar_query(query, *args, fetch=False, commit=False):
    conn = sqlite3.connect('jogos.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None
    try:
        cursor.execute(query, args)
        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()
    return resultado

# GET /jogos ou GET /jogos/<id>
@app.route('/jogos', methods=['GET'])
@app.route('/jogos/<int:id>', methods=['GET'])
def gerenciar_jogos(id=None):
    if id:
        jogo = executar_query("SELECT * FROM jogos WHERE id = ?", id, fetch=True)
        if jogo:
            return jsonify(dict(jogo[0])), 200
        return jsonify({"erro": "Jogo não encontrado"}), 404

    dados = executar_query("SELECT * FROM jogos", fetch=True)
    lista_jogos = [dict(item) for item in dados]
    return jsonify(lista_jogos), 200

   


# Editar jogo
@app.route('/edit/<int:id>',methods=['PUT'])
def edit_jogo(id):
    jogo = executar_query("SELECT * FROM jogos WHERE id = ?", id, fetch=True)
    if not jogo:
        return "Jogo não encontrado", 404
    dados = request.get_json()
    executar_query(
        "UPDATE jogos SET titulo = ?, plataforma = ?, preco = ?, estoque = ? WHERE id = ?",
        dados.get('titulo'), dados.get('plataforma'), dados.get('preco'), dados.get('estoque'), id,
        commit=True
    )
    return jsonify({"mensagem": "Jogo atualizado com sucesso!"}), 204

# POST /jogos
@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()
    executar_query(
        "INSERT INTO jogos (titulo, plataforma, preco, estoque) VALUES (?, ?, ?, ?)",
        dados.get('titulo'), dados.get('plataforma'), dados.get('preco'), dados.get('estoque'),
        commit=True
    )
    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201

# PUT /jogos/<id>
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()
    existe = executar_query("SELECT id FROM jogos WHERE id = ?", id, fetch=True)
    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "UPDATE jogos SET titulo = ?, plataforma = ?, preco = ?, estoque = ? WHERE id = ?",
        dados.get('titulo'), dados.get('plataforma'), dados.get('preco'), dados.get('estoque'), id,
        commit=True
    )
    return '', 204  # Status 204 sem conteúdo

# DELETE /jogos/<id>
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query("SELECT titulo FROM jogos WHERE id = ?", id, fetch=True)
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404
   

    executar_query("DELETE FROM jogos WHERE id = ?", id, commit=True)
    return jsonify({"mensagem": f"Jogo '{jogo[0]['titulo']}' removido!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
