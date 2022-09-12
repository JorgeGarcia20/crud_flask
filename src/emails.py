# import smtplib
# from decouple import config


# def bienvenida_nuevo_usuario(correo):
#     message = "Hola. bienvenido a mi pequeña tienda".encode('utf-8').strip()
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('fulanotest00@gmail.com', config('MAIL_PASSWORD'))
#     server.sendmail('fulanotest00@gmail.com', correo, message)
#     server.quit()

# from flask_mail import Message
# from flask import current_app, render_template


# def bienvenida_nuevo_usuario(mail, nombre_cliente, correo_cliente):
#     try:
#         message = Message(subject='Bienvenido a nuestra tienda', sender=current_app.config['MAIL_USERNAME'],
#                           recipients=[correo_cliente])
#         message.html = render_template(
#             'emails/bienvenida.html', cliente=nombre_cliente)
#         mail.send(message)
#     except Exception as ex:
#         raise Exception(ex)
