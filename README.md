# Relatório: Análise de Feedbacks dos Usuários

## 1. Estrutura da Aplicação

A aplicação foi desenvolvida em **Python 3.10+** utilizando **Flask** para o backend e **MySQL** como banco de dados. O objetivo principal é coletar feedbacks de usuários, classificá-los pelo sentimento (positivo, negativo ou inconclusivo) e identificar funcionalidades sugeridas.

### 1.1 Estrutura de Diretórios
```
feedback_analysis/
├── backend/
│   ├── app.py  # Arquivo principal da API
│   ├── models.py  # Definição das tabelas do banco de dados
│   ├── database.py  # Configuração do banco de dados
│   ├── routes.py  # Rotas da API
│   ├── services.py  # Lógica de classificação e extração de funcionalidades
│   ├── config.py  # Configurações gerais da aplicação
├── frontend/
│   ├── templates/
│   │   ├── index.html  # Página inicial com relatório dos feedbacks
│   ├── static/
│   │   ├── style.css  # Arquivo de estilos
│   ├── app.py  # Aplicativo Flask para exibir o frontend
├── .env  # Arquivo de variáveis de ambiente
├── requirements.txt  # Dependências da aplicação
├── README.md  # Documentação
```

## 2. Solução do Erro no MySQL

O erro **"ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)"** foi causado por:
1. O MySQL tentando autenticar com um usuário sem permissão.
2. Senha incorreta para o usuário `root`.

### 2.1 Solução Passo a Passo
1. **Tentar acessar com o usuário correto**
   ```bash
   mysql -u root -p
   ```
2. **Se a senha do root for desconhecida, redefini-la:**
   - **Linux:**
     ```bash
     sudo systemctl stop mysql
     sudo mysqld_safe --skip-grant-tables &
     mysql -u root
     ```
   - **Windows:**
     ```cmd
     net stop MySQL80
     mysqld --skip-grant-tables
     mysql -u root
     ```
   - **Alterar senha:**
     ```sql
     FLUSH PRIVILEGES;
     ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha';
     ```
   - **Reiniciar o MySQL:**
     ```bash
     sudo systemctl restart mysql  # Linux
     net start MySQL80  # Windows
     ```

## 3. Como Rodar a Aplicação em Outra Máquina

### 3.1 Passos Iniciais
1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seu-usuario/feedback_analysis.git
   cd feedback_analysis
   ```

2. **Criar e ativar um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instalar as dependências**
   ```bash
   pip install -r requirements.txt
   ```

### 3.2 Configurar o Banco de Dados
1. **Criar banco de dados no MySQL**
   ```sql
   CREATE DATABASE feedback_db;
   ```
2. **Configurar a conexão no `.env`**
   ```ini
   DB_URI=mysql+pymysql://root:senha@localhost/feedback_db
   ```
3. **Rodar as migrações para criar tabelas**
   ```bash
   flask db upgrade
   ```

### 3.3 Iniciar a Aplicação
1. **Rodar o backend**
   ```bash
   python backend/app.py
   ```
2. **Rodar o frontend**
   ```bash
   python frontend/app.py
   ```
3. **Acessar no navegador:**
   - API: [http://localhost:5000](http://localhost:5000)
   - Relatório: [http://localhost:5001](http://localhost:5001)

Caso haja dúvidas ou erros, me avise! 🚀

