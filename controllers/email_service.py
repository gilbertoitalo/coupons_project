import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import datetime
#from controllers import clients 


load_dotenv()
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SENHA_LOGIN = os.getenv("SENHA_LOGIN")
HOST = os.getenv('HOST') 
PORTA = os.getenv('PORTA') #587

def gerar_arquivo_log_erro(log_erros):
    data_hora_atual = datetime.datetime.today().strftime('%d_%m_%y_%H_%M_%S')
    
        

#anivers= clients.mostrar_por_aniver

#def ver_anivers(anivers):
   #print("Os aniversariantes são esses: ")
#for cliente in anivers:
   #print(f"Nome: {cliente['nome_completo']}, E-mail: {cliente['email']}")
   

def enviar_emails():
   log_erros = []
   emails_enviados = 0 
   #inserir infos do servidor
   servidor = smtplib.SMTP('smtp.gmail.com', 587)
   servidor.starttls()
   servidor.login('italo.mpinheiro@gmail.com','ifcpshvmwqdgwgzn')

   msg = MIMEMultipart()
   msg ['from'] = 'italo.mpinheiro@gmail.com'
   msg ['to'] = 'gilberto_italo@hotmail.com'
   msg ['Subject'] = 'primeiro teste'

   conteudo_email = MIMEText('teste' ,'plain')
   msg.attach(conteudo_email)

   servidor.send_message(msg)
   servidor.quit()

   msg.attach

enviar_emails()
   

def exibir_destinarios(recebedor):
    if len(anivers) > 0:
        print(f"Ha" + len(anivers)+"para ser enviados ")
    else:
        print("Nao ha aniver para enviar")
        
    if len(anivers) > 0:
     while True:
      opcao = input("Desejar envia-los ou ver seus destinatários? Digite enviar ou ver: ")
      if opcao == "enviar":
         ver_anivers(anivers)
      elif opcao == "enviar":
         enviar_emails(anivers)
      else:
         print("Opcao invalida. Opcao desconhecida")
         
