from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from config import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM="no-reply@alumind.com",
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_TLS=True,
    MAIL_SSL=False
)

async def send_weekly_summary(email_to: str, summary: str):
    message = MessageSchema(
        subject="Resumo Semanal de Feedbacks",
        recipients=[email_to],
        body=summary,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
