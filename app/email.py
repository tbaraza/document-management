from app import mail
from flask.ext.mail import Message
from config import Config
from flask import render_template


def send_email(to, subject, template, **kwargs):
    msg = Message(Config['DOCUMENT_MANAGEMENT_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=Config['DOCUMENT_MANAGEMENT_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
