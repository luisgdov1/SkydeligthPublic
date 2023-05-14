from django.template.loader import render_to_string
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_reset(email, name, url_personal):
    contexto = {"url_personal" : url_personal, "nombre": name}
    html_text = render_to_string('email.html', contexto)
    message = Mail(
        from_email="soporteskydelight@gmail.com",
        to_emails= email,
        subject='Recuperacion de contraseña',
        html_content= html_text,)
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API)
        response = sg.send(message)
        if response.status_code != 202:
            return False
        else:
            return True
    except Exception as e:
        return False

