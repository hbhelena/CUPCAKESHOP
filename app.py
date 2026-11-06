from flask import Flask, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_pit' # Obrigatório para usar o carrinho (session)

def iniciar_banco():
    conn = sqlite3.connect('cupcakeshop.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS produto')
    cursor.execute('''
        CREATE TABLE produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            imagem TEXT
        )
    ''')
    cupcakes_iniciais = [
        ("Baunilha com Laranja", "Cupcake de baunilha suave com raspas de laranja.", 8.50, "https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?q=80&w=300&auto=format&fit=crop"),
        ("Chocomenta", "Massa de chocolate com cobertura refrescante de menta.", 7.50, "https://images.unsplash.com/photo-1587668178277-295251f900ce?q=80&w=300&auto=format&fit=crop"),
        ("Morango", "Cupcake de morango com cobertura especial.", 9.00, "https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?q=80&w=300&auto=format&fit=crop")
    ]
    cursor.executemany('INSERT INTO produto (nome, descricao, preco, imagem) VALUES (?, ?, ?, ?)', cupcakes_iniciais)
    conn.commit()
    conn.close()

iniciar_banco()

@app.route('/')
def catalogo():
    conn = sqlite3.connect('cupcakeshop.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produto')
    cupcakes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    # Conta quantos itens tem no carrinho para mostrar no topo da tela
    total_itens = len(session.get('carrinho', []))
    
    return render_template('index.html', cupcakes=cupcakes, total_itens=total_itens)

@app.route('/adicionar/<int:id_produto>')
def adicionar(id_produto):
    # Pega o carrinho atual ou cria uma lista vazia, adiciona o item e salva
    carrinho = session.get('carrinho', [])
    carrinho.append(id_produto)
    session['carrinho'] = carrinho
    return redirect(url_for('catalogo'))

@app.route('/carrinho')
def ver_carrinho():
    carrinho_ids = session.get('carrinho', [])
    produtos_carrinho = []
    total = 0.0
    
    if carrinho_ids:
        conn = sqlite3.connect('cupcakeshop.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        for pid in carrinho_ids:
            cursor.execute('SELECT * FROM produto WHERE id = ?', (pid,))
            prod = dict(cursor.fetchone())
            produtos_carrinho.append(prod)
            total += prod['preco']
        conn.close()
        
    return render_template('carrinho.html', produtos=produtos_carrinho, total=total, total_itens=len(carrinho_ids))

@app.route('/finalizar')
def finalizar():
    # Limpa o carrinho simulando que o pedido foi concluído
    session.pop('carrinho', None)
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)
