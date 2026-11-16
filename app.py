from flask import Flask, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_pit'

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
    produtos = [
        ('Chocolate Branco', 'Cupcake de baunilha com cobertura cremosa de chocolate branco e granulados.', 8.50, 'img/chocolatebranco-com-granulados.jpg'),
        ('Chocomenta', 'Massa de chocolate com cobertura refrescante de menta.', 7.50, 'img/chocomenta.jpg'),
        ('Morango Imperial', 'Cupcake artesanal com cobertura cremosa e morango fresco no topo.', 9.00, 'img/morango.jpg'),
        ('Red Velvet', 'Massa aveludada de cacau com cobertura cremosa de cream cheese.', 9.50, 'img/redvelvet.jpg'),
        ('Chocolate Intenso', 'Massa fofinha de cacau com ganache de chocolate e confeitos coloridos.', 8.00, 'img/chocolate.jpg'),
        ('Pistache com Chocolate', 'Massa de chocolate com creme artesanal de pistache. O favorito da casa!', 10.50, 'img/pistache-massa-de-chocolate.jpg')
    ]
    cursor.executemany('INSERT INTO produto (nome, descricao, preco, imagem) VALUES (?, ?, ?, ?)', produtos)
    conn.commit()
    conn.close()

iniciar_banco()

@app.route('/')
def index():
    conn = sqlite3.connect('cupcakeshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produto')
    produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar/<int:id>')
def adicionar(id):
    if 'carrinho' not in session:
        session['carrinho'] = []
    carrinho = list(session['carrinho'])
    carrinho.append(id)
    session['carrinho'] = carrinho
    return redirect(url_for('index'))

@app.route('/carrinho')
def carrinho():
    ids = session.get('carrinho', [])
    conn = sqlite3.connect('cupcakeshop.db')
    cursor = conn.cursor()
    itens = []
    total = 0.0
    for item_id in ids:
        cursor.execute('SELECT * FROM produto WHERE id = ?', (item_id,))
        prod = cursor.fetchone()
        if prod:
            itens.append(prod)
            total += prod[3]
    conn.close()
    return render_template('carrinho.html', itens=itens, produtos=itens, total=total)

@app.route('/finalizar')
def finalizar():
    session.pop('carrinho', None)
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)