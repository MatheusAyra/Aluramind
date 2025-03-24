from flask import Flask
from backend.database import db, init_db  # Certifique-se que o caminho está correto
import backend.models  # Isso garante que as tabelas do banco sejam reconhecidas
import config

app = Flask(__name__)
app.config.from_object(config)  # Carregar configurações do banco

# Inicializar o banco de dados
db.init_app(app)
init_db(app)

if __name__ == "__main__":
    app.run(debug=True)

