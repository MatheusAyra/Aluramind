from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "seu_email@gmail.com"
app.config["MAIL_PASSWORD"] = "sua_senha"

mail = Mail(app)

def send_weekly_report(email, report_data):
    with app.app_context():
        msg = Message("Resumo Semanal de Feedbacks", sender="seu_email@gmail.com", recipients=[email])
        msg.body = f"""
        Feedbacks Positivos: {report_data['positive_percentage']}%
        Funcionalidades Mais Pedidas:
        {report_data['top_requested_features']}
        """
        mail.send(msg)
