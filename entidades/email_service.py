import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import datetime
from repositorio.clients import get_mostrar_aniver

#TO DO criar uma def de log_err para gerar o arq em com qualquer erro

load_dotenv()
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SENHA_LOGIN = os.getenv("SENHA_LOGIN")
HOST = os.getenv('HOST') 
PORTA = os.getenv('PORTA') 

# def gerar_arquivo_log_erro(log_erros):
#     data_hora_atual = datetime.datetime.today().strftime('%d_%m_%y_%H_%M_%S')
    
        

#anivers= clients.mostrar_por_aniver

#def ver_anivers(anivers):
   #print("Os aniversariantes são esses: ")
#for cliente in anivers:
   #print(f"Nome: {cliente['nome_completo']}, E-mail: {cliente['email']}")
   
# TO DO criar logica para chamar os aniver e mandar    


def enviar_emails():
   
   clientes= []

   # with open('clientes.csv', 'r') as csv_file:
   #      reader = csv.DictReader(csv_file)
   #      for row in reader:
   #          clientes.append(row)

   hoje = datetime.date.today()    
   clientes_aniver = get_mostrar_aniver()

   if clientes_aniver is not None:
    print(f"Numeros de clientes fazendo anive hj sao: {len(clientes_aniver)}")
    for cliente in clientes_aniver:
      print(f"Name: {clientes['nome_completo']}, Email: {clientes['email']}")
      
   else:
      print("Nao foi encontrado nenhum cliente fazendo aniver hoje")
   
   
   opcao = input("Digite 'enviar' para enviar os email or 'ver' polharara  os destinatarios: ")

   if opcao.lower() == 'enviar':
      for clientes in get_mostrar_aniver:
        enviar_emails(clientes)
        print("Emails de aniver enviado com sucesso")

   elif opcao.lower() == 'ver':
      for clientes in get_mostrar_aniver:
         print(f"Name: {clientes['nome_completo']}, Email: {clientes['email']}")
   else:
      print("Acao invaldia")
      
   
   receptor_email = clientes['email']
   receptor_email_nome = clientes["nome_completo"].split()[0]                         
   titulo_email = f"Feliz aniversário!, {receptor_email_nome}!"
   escopo = f"Olá, <receptor_email_nome>. Nós da Serasa Experan te desejamos um feliz aniversário. Aqui está um cupom de desconto para utilizar nas compras de nossos produtos e serviços: {cupom_desconto}"

   #inserir infos do servidor SMTP
   # servidor = smtplib.SMTP('smtp.gmail.com', 587)
   # servidor.starttls()
   # servidor.login('italo.mpinheiro@gmail.com','ifcpshvmwqdgwgzn')

   msg = MIMEMultipart()
   msg ['from'] = 'italo.mpinheiro@gmail.com'
   msg ['to'] = 'gilberto_italo@hotmail.com'
   msg ['Subject'] = titulo_email

   conteudo_email = MIMEText(escopo ,'plain')
   msg.attach(conteudo_email)

   
   with smtplib.SMTP(HOST, PORTA) as servidor:
      servidor.starttls()
      servidor.login(EMAIL_LOGIN,SENHA_LOGIN)
      servidor.send_message(msg)

      print(f"Email foi enviado para {receptor_email}")

enviar_emails()
 
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
         

