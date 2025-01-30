# Level Up - API FastAPI

Este projeto é uma API desenvolvida com **FastAPI** para gerenciar personagens em um jogo. A API permite a criação, listagem e consulta de personagens no banco de dados.

## Tecnologias Utilizadas
- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **SQLite (ou outro banco de dados suportado)**
- **Uvicorn** (para executar a API)

## Estrutura do Projeto
```
Level_Up/
│-- fastapi_game/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── crud.py          # Funções para interagir com o banco de dados
│   ├── database.py      # Configuração do banco de dados
│   ├── models.py        # Modelos do SQLAlchemy
│   ├── schemas.py       # Definição dos esquemas Pydantic
│   └── __init__.py
│
└── .venv/               # Ambiente virtual
```

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/1mperador/Level_Up.git
   cd Level_Up
   ```
2. Ative o ambiente virtual:
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a API:
   ```bash
   uvicorn fastapi_game.main:app --reload
   ```
5. Acesse a documentação interativa no navegador:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints Principais
- **Criar um personagem:** `POST /characters/`
- **Listar personagens:** `GET /characters/`
- **Obter um personagem por ID:** `GET /characters/{character_id}`

## Contribuição
Sinta-se à vontade para contribuir com melhorias e novas funcionalidades! Abra uma issue ou envie um pull request.

## Licença
Este projeto está sob a licença MIT.

