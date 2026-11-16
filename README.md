# Cupcake Shop

Projeto Integrador Transdisciplinar em Engenharia de Software II desenvolvido para o curso de Engenharia de Software da Cruzeiro do Sul Virtual.

## Tecnologias

### Frontend (View)
- HTML5
- CSS3
- Jinja2 (Templates dinâmicos)

### Backend (Controller & Model)
- Python 3
- Flask
- SQLite3 (Persistência relacional nativa)
- Unittest (Testes automatizados)

## Estrutura do Projeto

- `app.py` — Controlador principal, rotas HTTP, regras de negócio e inicialização do banco SQLite
- `cupcakeshop.db` — Banco de dados físico relacional SQLite
- `test_app.py` — Suíte de testes unitários e de integração automatizados
- `templates/` — Camada de visualização (IHC)
  - `index.html` — Vitrine e catálogo de cupcakes
  - `carrinho.html` — Gestão dos itens na sessão e soma de valores
  - `sucesso.html` — Confirmação de fechamento do pedido

## Funcionalidades

- Catálogo dinâmico de cupcakes integrado ao banco de dados
- Adição de produtos ao carrinho com contador em tempo real na sessão
- Cálculo automático de subtotal e total do pedido
- Finalização de pedido simulada com limpeza automática de sessão
- Criação e carga inicial automática do banco de dados na primeira execução

---

## Situação-Problema 1: IHC e Dicionário de Dados

### Interface Humano-Computador (IHC)
A interface foi projetada seguindo princípios de usabilidade, clareza, consistência visual e feedback imediato ao usuário, dividindo a jornada em três telas enxutas (`index.html`, `carrinho.html` e `sucesso.html`).

### Projeto Físico e Dicionário de Dados (SQLite)
O banco de dados físico é gerenciado pelo arquivo `cupcakeshop.db` através da tabela `produto`:

| Atributo | Tipo de Dado (SQLite) | Restrição / Domínio | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do cupcake |
| `nome` | TEXT | NOT NULL | Nome comercial do sabor do cupcake |
| `descricao` | TEXT | NULL | Detalhamento dos ingredientes e cobertura |
| `preco` | REAL | NOT NULL | Valor unitário de venda em Reais (R$) |
| `imagem` | TEXT | NULL | URL da fotografia ilustrativa do produto |

---

## Situação-Problema 2: Instalação e Manual de Uso

### Pré-requisitos
Para executar o projeto localmente é necessário ter instalado:
- Python 3.x
- Pip (gerenciador de pacotes do Python)

O projeto utiliza SQLite como banco de dados relacional. Não é necessário instalar ou configurar um servidor de banco de dados separadamente, pois a tabela e os produtos iniciais são gerados automaticamente ao iniciar a aplicação.

### 1. Clonar o repositório
```bash
git clone [https://github.com/hbhelena/CUPCAKESHOP.git](https://github.com/hbhelena/CUPCAKESHOP.git)
cd CUPCAKESHOP
