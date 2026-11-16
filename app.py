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
        ('Baunilha com Laranja', 'Cupcake de baunilha suave com raspas de laranja.', 8.50, 'https://images.unsplash.com/photo-1519869325930-281384150729?w=500'),
        ('Chocomenta', 'Massa de chocolate com cobertura refrescante de menta.', 7.50, 'https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=500'),
        ('Morango', 'Cupcake de morango com cobertura especial.', 9.00, 'https://images.unsplash.com/photo-1587668178277-295251f900ce?w=500'),
        ('Red Velvet', 'Massa aveludada de cacau com cobertura cremosa de cream cheese.', 9.50, 'https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?w=500'),
        ('Caramelo Salgado', 'Cupcake amanteigado com recheio e cobertura de caramelo artesanal.', 8.00, 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?w=500'),
        ('Pistache Imperial', 'Massa fofinha com ganache de pistache importado. O favorito da casa!', 10.50, 'https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=500')
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