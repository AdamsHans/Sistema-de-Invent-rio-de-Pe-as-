# Sistema de Gestão de Almoxarifado com Django

Este projeto é um sistema de controle de estoque desenvolvido em **Django**, focado na gestão de um almoxarifado. Ele permite registrar e acompanhar o fluxo de peças (entradas, saídas, empréstimos) e exportar essas informações para arquivos CSV diretamente pelo Django Admin.

## 📦 Funcionalidades

- Visualização e controle de estoque atual
- Registro de entradas e saídas de peças
- Gerenciamento de peças zeradas
- Controle de empréstimos (peças enviadas e recebidas)
- Exportação de dados para arquivos CSV

## 🧠 Tecnologias Utilizadas

- Python
- Django
- Django Admin
- CSV para exportação de dados

## 🗃️ Modelos e Exportações

O sistema possui os seguintes modelos registrados no Django Admin:

### `EstoqueAtual`
- Campos: `numero_cep`, `sp_number`, `produto`, `local`, `quantidade`
- Ação: Exportar estoque atual para CSV

### `Entrada`
- Campos: `numero_cep`, `sp_number`, `produto`, `local`, `quantidade`, `data`, `observacoes`
- Ação: Exportar entradas para CSV

### `Saida`
- Campos: `numero_cep`, `sp_number`, `produto`, `local`, `quantidade`, `data`, `observacoes`
- Ação: Exportar saídas para CSV

### `ItemZerado`
- Campos: `numero_cep`, `sp_number`, `produto`, `local`, `quantidade`
- Ação: Exportar itens zerados para CSV

### `Emprestimo`
- Campos: `tipo`, `numero_cep`, `sp_number`, `produto`, `quantidade`, `data`, `observacoes`
- Ação: Exportar empréstimos para CSV

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse o diretório do projeto:

cd nome-do-projeto

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale os requisitos:

pip install -r requirements.txt

Rode as migrações:

python manage.py migrate

Crie um superusuário:

python manage.py createsuperuser

Inicie o servidor:

python manage.py runserver

Acesse o Django Admin:

http://127.0.0.1:8000/admin

📂 Exportação de Dados
As ações de exportação estão disponíveis no Django Admin, como ações personalizadas nos modelos. Basta selecionar os registros desejados e escolher a opção de exportar para CSV.

Os arquivos gerados são compatíveis com editores como Excel e LibreOffice.

👨‍💻 Autor
Desenvolvido por Adams Hans Alexssei Costa Monteiro
📫 Email: adamsmonteiro@hotmail.com
🔗 LinkedIn: https://www.linkedin.com/in/adamshans/


