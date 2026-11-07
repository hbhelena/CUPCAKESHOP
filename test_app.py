import unittest
from app import app, iniciar_banco
import sqlite3

class TestCupcakeShop(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        iniciar_banco()

    def test_1_banco_de_dados_produtos(self):
        conn = sqlite3.connect('cupcakeshop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM produto')
        total = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(total, 3)

    def test_2_carregamento_catalogo(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Baunilha com Laranja'.encode('utf-8'), response.data)

    def test_3_fluxo_carrinho_e_finalizacao(self):
        self.client.get('/adicionar/1', follow_redirects=True)
        response_carrinho = self.client.get('/carrinho')
        self.assertEqual(response_carrinho.status_code, 200)
        self.assertIn('R$ 8.50'.encode('utf-8'), response_carrinho.data)

        response_finalizar = self.client.get('/finalizar')
        self.assertEqual(response_finalizar.status_code, 200)
        self.assertIn('Pedido Realizado!'.encode('utf-8'), response_finalizar.data)

if __name__ == '__main__':
    unittest.main()
    