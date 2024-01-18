from django.shortcuts import render
from users.forms import CustomAuthenticationForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages

def login(request):

    form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def index(request):

    if request.method == 'GET':

        return render(request, 'inicio/index.html')

    elif request.method == 'POST':

        nome_completo = request.POST['name']
        email = request.POST['email']
        telefone = request.POST['telefone']

        subject = 'Formulário do Portfolio'
        body = f'Nome completo: {nome_completo}\nE-mail: {email}\nTelefone: {telefone}'

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'lucasreinert96@gmail.com'
        smtp_password = 'odzf tcau fcso jsol'

        # Configuração do servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Criação do e-mail
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = 'lucasreinert96@gmail.com'
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(smtp_username, 'lucasreinert96@gmail.com', msg.as_string())

        server.quit()

        messages.success(request, 'E-mail enviado com sucesso!')
        return render(request, 'redirect/redirect_index.html')

    return render(request, 'inicio/index.html')

def index_en(request):

    if request.method == 'GET':

        return render(request, 'inicio/index_en.html')

    elif request.method == 'POST':

        nome_completo = request.POST['name']
        email = request.POST['email']
        telefone = request.POST['telefone']

        subject = 'Formulário do Portfolio'
        body = f'Nome completo: {nome_completo}\nE-mail: {email}\nTelefone: {telefone}'

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'lucasreinert96@gmail.com'
        smtp_password = 'odzf tcau fcso jsol'

        # Configuração do servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Criação do e-mail
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = 'lucasreinert96@gmail.com'
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(smtp_username, 'lucasreinert96@gmail.com', msg.as_string())

        server.quit()

        messages.success(request, 'E-mail enviado com sucesso!')
        return render(request, 'redirect/redirect_index_en.html')

    return render(request, 'inicio/index_en.html')