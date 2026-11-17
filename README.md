# 🧁 Sweet Cupcake — Confeitaria Artesanal (E-commerce Web)

# 🧁 Sweet Cupcake — Confeitaria Artesanal (E-commerce Web)

Aplicação web de loja virtual de cupcakes desenvolvida em **Python (Flask)** com banco de dados relacional **SQLite**, projetada como entrega prática da disciplina de Engenharia de Software.

🔗 **Aplicação no ar (Deploy):** https://hbhelena.pythonanywhere.com/  
💻 **Repositório GitHub:** https://github.com/hbhelena/CUPCAKESHOP  
👩‍💻 **Autora:** Karen Helena Brabo da Silva

---

## 📋 Sobre o Projeto

A **Sweet Cupcake** é uma plataforma de vitrine e vendas online de cupcakes artesanais que aplica princípios de Engenharia de Software, Usabilidade (IHC) e Testes de Software:

- **Catálogo Dinâmico:** Exibição de 6 sabores artesanais carregados diretamente do banco de dados SQLite (`cupcakeshop.db`), com imagens locais otimizadas, descrições, preços e selos visuais de destaque (*Mais Pedido*, *Favorito* e controle visual de item *Esgotado*).
- **Carrinho de Compras em Sessão:** Adição rápida de produtos com contador atualizado em tempo real no cabeçalho, listagem detalhada com miniaturas e cálculo automático do valor total do pedido.
- **Checkout Simulado:** Fluxo completo de finalização de compra (`/finalizar`) com limpeza automática da sessão do carrinho e tela de confirmação de pedido.
- **Feedback de Usuários:** Modal interativo flutuante (*Avaliar o site*) para coleta de avaliações e notas de experiência de uso.
- **Design Responsivo (Mobile & Desktop):** Interface em paleta pastel responsiva, adaptada para telas de smartphones e computadores.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3, Flask
- **Banco de Dados:** SQLite3 (`cupcakeshop.db`)
- **Front-end:** HTML5, CSS3 (Grid Layout, Flexbox e Media Queries), JavaScript
- **Testes Automatizados:** Biblioteca `unittest` nativa do Python (`test_app.py`)
- **Hospedagem / Deploy em Nuvem:** PythonAnywhere

---

## 🗄️ Arquitetura e Dicionário de Dados

### Estrutura de Diretórios

    CUPCAKESHOP/
    ├── app.py                 # Aplicação Flask, rotas e inicialização do banco SQLite
    ├── test_app.py            # Suite de testes automatizados (unittest)
    ├── cupcakeshop.db         # Banco de dados relacional SQLite
    ├── README.md              # Documentação técnica do projeto
    ├── static/
    │   └── img/               # Fotografias locais dos 6 cupcakes do catálogo
    └── templates/
        ├── index.html         # Vitrine principal e modal de avaliação
        ├── carrinho.html      # Revisão de itens e cálculo do total do pedido
        └── sucesso.html       # Confirmação de pedido finalizado

### Tabela `produto` (SQLite)

| Campo | Tipo | Restrição | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único do cupcake |
| `nome` | `TEXT` | `NOT NULL` | Nome do sabor do cupcake |
| `descricao` | `TEXT` | — | Descrição detalhada dos ingredientes |
| `preco` | `REAL` | `NOT NULL` | Preço unitário em reais (R$) |
| `imagem` | `TEXT` | — | Caminho relativo da imagem em `static/img/` |

---

## 🚀 Como Executar o Projeto Localmente

    # 1. Clonar o repositório
    git clone https://github.com/hbhelena/CUPCAKESHOP.git
    cd CUPCAKESHOP

    # 2. Instalar a dependência do Flask
    pip install flask

    # 3. Iniciar o servidor local
    python app.py

Acesse no navegador: `http://127.0.0.1:5000`

---

## 🧪 Testes de Software e Validação com Usuários

### 1. Testes Automatizados de Unidade e Integração (`unittest`)
Para executar a bateria de testes automatizados que valida a rota principal, o carregamento do banco de dados, a adição de itens na sessão e o cálculo no carrinho:

    python -m unittest test_app.py

### 2. Testes de Usabilidade com Usuários Reais e Melhorias Aplicadas
O sistema publicado em produção (`hbhelena.pythonanywhere.com`) foi submetido à avaliação prática de usuários externos em dispositivos Desktop e Mobile. A partir dos feedbacks coletados, foram implementadas as seguintes melhorias corretivas:

1. **Correção de renderização das miniaturas no carrinho:** Ajuste do mapeamento `url_for('static', filename=item[4])` no template `carrinho.html` para exibição das fotos dos produtos adicionados.
2. **Correção de responsividade (Overflow no Header Mobile):** Inclusão de regras `@media (max-width: 600px)` e `overflow-x: hidden` para ajustar o cabeçalho em telas estreitas (360px), eliminando o corte lateral do botão do carrinho e empilhando os botões de ação no mobile. 