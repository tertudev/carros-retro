# 🚗 Carros Retrô

Plataforma web para catalogação, gerenciamento de inventário e enriquecimento de dados de veículos clássicos utilizando Inteligência Artificial.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🧐 Sobre o Projeto

O **Carros Retrô** é um sistema web robusto desenvolvido sob o padrão arquitetural **MVT (Model-View-Template)** do Django. O objetivo principal da aplicação é permitir o cadastro e a manutenção de um catálogo de carros clássicos, integrando recursos modernos de automação e inteligência artificial.

### Diferenciais Técnicos e Arquitetura:
*   **Desacoplamento com Django Signals:** O sistema utiliza *Signals* (`cars/signals.py`) para executar tarefas em segundo plano e manter a integridade dos dados. Ao cadastrar ou remover um veículo, o inventário (`CarInventory`) é recalculado de forma reativa.
*   **Integração com LLM (OpenAI):** Através de um client customizado (`openai_api/client.py`), o sistema consome a API da OpenAI para gerar automaticamente uma biografia histórica detalhada (`car_bio`) para cada veículo cadastrado, enriquecendo a experiência do usuário sem esforço manual.
*   **Autenticação Segura:** Módulo exclusivo de controle de acesso (`accounts`) que gerencia o fluxo de registro, login e permissões de usuários na plataforma.

## ✨ Funcionalidades

*   **Autenticação de Usuários:** Fluxo completo de registro, login e logout com validação de credenciais.
*   **CRUD de Veículos:** Cadastro, visualização de detalhes, edição e exclusão de carros clássicos com suporte a upload de imagens.
*   **Gerenciamento de Marcas:** Cadastro de fabricantes (`Brand`) associados aos veículos por meio de chaves estrangeiras.
*   **Geração de Bio via IA:** Integração com a API da OpenAI para gerar descrições históricas automáticas baseadas no modelo e ano do carro.
*   **Painel de Inventário:** Atualização dinâmica da quantidade de carros em estoque e valor total do inventário via banco de dados.

## 🛠️ Tecnologias

*   **Linguagem:** Python 3.11+
*   **Framework Web:** Django 6.0
*   **Banco de Dados:** PostgreSQL (suporte nativo via `psycopg2`) / SQLite (desenvolvimento)
*   **Processamento de Imagens:** Pillow 12.0
*   **Integração de IA:** OpenAI SDK v2.26
*   **Variáveis de Ambiente:** Python-dotenv

## 📂 Estrutura do Projeto

```text
├── accounts/          # App de autenticação e gerenciamento de usuários
├── app/               # Configurações globais do projeto Django (settings, urls, wsgi)
├── cars/              # App principal (regras de negócio, models de carros, marcas e inventário)
│   ├── migrations/    # Histórico de migrações do banco de dados
│   ├── templates/     # Páginas HTML do fluxo de CRUD de veículos
│   ├── forms.py       # Formulários de validação de dados
│   └── signals.py     # Triggers de inventário e chamadas de IA
├── media/             # Diretório de armazenamento de uploads (fotos dos carros)
├── openai_api/        # Módulo de integração com o serviço da OpenAI
├── manage.py          # CLI de gerenciamento do Django
└── requirements.txt   # Dependências do projeto
```

## 🚀 Como Começar

### Pré-requisitos

*   Python 3.11 ou superior instalado.
*   Chave de API da OpenAI (opcional, necessária apenas para a geração automática de biografias).

### Instalação e Configuração

1.  **Clonar o repositório:**
    ```bash
    git clone https://github.com/tertudev/carros-retro.git
    cd carros-retro
    ```

2.  **Criar e ativar o ambiente virtual (venv):**
    ```bash
    python -m venv venv
    # No Linux/macOS:
    source venv/bin/activate
    # No Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    ```

3.  **Instalar as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:
    ```env
    SECRET_KEY=sua_secret_key_django
    DEBUG=True
    OPENAI_API_KEY=sua_chave_da_openai
    ```

5.  **Executar as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Criar um usuário administrador (Superuser):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Iniciar o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

Acesse a aplicação em `http://127.0.0.1:8000/`.

## 🤝 Contribuição

Contribuições são bem-vindas para melhorar a arquitetura, adicionar testes ou novas features.

1. Faça um **Fork** do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Envie suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o **Push** da branch (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

## 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

Vamos codar o futuro! 🚀
