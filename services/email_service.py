              
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

from models.clients import *

load_dotenv()
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SENHA_LOGIN = 'mfbhohutakcdsjik'
HOST = os.getenv('HOST') 
PORTA = 587

# def gerar_arquivo_log_erro(log_erros):
#     data_hora_atual = datetime.datetime.today().strftime('%d_%m_%y_%H_%M_%S')
    
        

#anivers= clients.mostrar_por_aniver

#def ver_anivers(anivers):
   #print("Os aniversariantes são esses: ")
#for cliente in anivers:
   #print(f"Nome: {cliente['nome_completo']}, E-mail: {cliente['email']}")
   
# TO DO criar logica para chamar os aniver e mandar    

def send_emails():
   clients = []
   with open('clientes.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            clients.append(row)   
   #anivers = get_mostrar_aniver()
   today = datetime.today
   

   anivers = [cliente for cliente in clients] if get_all_anivers(clients['data_nascimento']) == today else print("Nennhum aniver hoje")


   
   if anivers is not None:
    print(f"Numeros de clientes fazendo anive hj sao: {len(anivers)}")
    for aniver in anivers:
      print(f"Name: {clients['nome_completo']}, Email: {clients['email']}")
      
   print(print(f"Numeros de anivers para ser enviado hoje é: {len(anivers)}"))
   
   
   option = input("Digite 'enviar' para enviar os email or 'ver' polharara  os destinatarios: ")

   if option.lower() == 'enviar':
      for anivers in clients:
         sending_email(anivers)

      print("Email enviado com sucesso")
      
      # for aniver in anivers:
      #   enviar_emails(clientes)
      #   print("Emails de aniver enviado com sucesso")

   elif option.lower() == 'ver':
      for clients in get_all_anivers:
         print(f"Name: {clients['nome_completo']}, Email: {clients['email']}")
   else:
      print("Acao invaldia")
      


def sending_email(anivers):
   
   sent_emails = 0 
   
   server = smtplib.SMTP(HOST, PORTA)

   server.starttls()

   server.login(EMAIL_LOGIN, SENHA_LOGIN)


   msg = MIMEMultipart()
   msg ['from'] = EMAIL_LOGIN
   msg ['to'] = anivers('email')
   msg ['Subject'] = titulo_email
   
   
   receptor_email_nome = anivers["nome_completo"].split()[0]                         
   titulo_email = f"Feliz aniversário!, {receptor_email_nome}!"
   conteudo_email = MIMEText(escopo ,'plain')
   msg.attach(conteudo_email)
   escopo = f"Olá, <receptor_email_nome>. Nós da Serasa Experan te desejamos um feliz aniversário. Aqui está um cupom de desconto para utilizar nas compras de nossos produtos e serviços: "
   try:
      server.send_message(msg)
      sent_emails += 1
   except:
      pass
   finally:
      server.quit()
      return sent_emails
   

   

   
   # with smtplib.SMTP(HOST, PORTA) as servidor:
   #    servidor.starttls()
   #    servidor.login(EMAIL_LOGIN,SENHA_LOGIN)
   #    servidor.send_message(msg)

      #print(f"Email foi enviado para {receptor_email}")



 
#    for destinatario  in destinatarios:
#       primeiro_nome = destinario.split("")[0]
#       corpo_personalizado = escopo.replace('<primeiro_nome', primeiro_nome)
#       msg["To"] = destinario
#       msg.attach(MIMEText(escopo, "plain"))

#       servidor.send_message(msg)
#       servidor.quit()
   

# def exibir_destinarios(recebedor):
#     if len(aniversariantes) > 0:
#         print(f"Ha" + len(anivers)+"para ser enviados ")
#     else:
#         print("Nao ha aniver para enviar")
        
#     if len(anivers) > 0:
#      while True:
#       opcao = input("Desejar envia-los ou ver seus destinatários? Digite enviar ou ver: ")
#       if opcao == "enviar":
#          ver_anivers(anivers)
#       elif opcao == "enviar":
#          enviar_emails(anivers)
#       else:
#          print("Opcao invalida. Opcao desconhecida")
         

