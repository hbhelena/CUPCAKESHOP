# Cupcake Shop - Projeto Integrador Transdisciplinar em Engenharia de Software II

Aplicação web de e-commerce para venda de cupcakes desenvolvida em Python (Flask) com banco de dados relacional SQLite, utilizando o padrão arquitetural MVC (Model-View-Controller).

---

## Situação-Problema 1: Planejamento, IHC e Banco de Dados

### Escopo e Interface Humano-Computador (IHC)
A interface foi projetada seguindo princípios de usabilidade, clareza, consistência visual e feedback imediato ao usuário:
- **Catálogo Principal (`index.html`):** Exibição em grade (grid) limpa com imagem, descrição clara, preço formatado e ação direta de adição.
- **Carrinho de Compras (`carrinho.html`):** Listagem de itens selecionados na sessão, cálculo automático de subtotal e botão de confirmação.
- **Confirmação de Pedido (`sucesso.html`):** Retorno visual imediato confirmando a conclusão do fluxo e limpando a sessão.

### Projeto Físico e Dicionário de Dados (SQLite)
O banco de dados físico é gerenciado pelo arquivo `cupcakeshop.db`.

**Tabela:** `produto`

| Atributo | Tipo de Dado (SQLite) | Restrição / Domínio | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do cupcake |
| `nome` | TEXT | NOT NULL | Nome comercial do sabor do cupcake |
| `descricao` | TEXT | NULL | Detalhamento dos ingredientes e cobertura |
| `preco` | REAL | NOT NULL | Valor unitário de venda em Reais (R$) |
| `imagem` | TEXT | NULL | URL da fotografia ilustrativa do produto |

---

## Situação-Problema 2: Arquitetura MVC, Codificação e Manual de Uso

### Arquitetura em Camadas (MVC)
- **Model (Modelo):** Persistência relacional em SQLite (`cupcakeshop.db`) com criação e carga inicial automatizadas na função `iniciar_banco()`.
- **View (Visão):** Templates dinâmicos renderizados via Jinja2 (`templates/index.html`, `templates/carrinho.html`, `templates/sucesso.html`) estilizados em CSS3.
- **Controller (Controlador):** Rotas de controle e regras de negócio gerenciadas no arquivo `app.py` (`/`, `/adicionar/<id>`, `/carrinho`, `/finalizar`).

### Manual de Uso da Aplicação
1. **Pré-requisitos:** Possuir o Python 3 e o pacote Flask instalados (`pip install flask`).
2. **Inicialização:** No terminal, dentro da pasta do projeto, execute:
   ```bash
   python app.py
   