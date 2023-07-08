import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv
import datetime
from controllers import clients 

def gerar_arquivo_log_erro(log_erros):
    data_hora_atual = datetime.datetime.today().strftime('%d_%m_%y_%H_%M_%S')
    
        

anivers= clients.mostrar_por_aniver

def ver_anivers(anivers):
   print("Os aniversariantes são esses: ")
for cliente in anivers:
   print(f"Nome: {cliente['nome_completo']}, E-mail: {cliente['email']}")
   

def enviar_email(anivers):
   log_erros = []
   emails_enviados = 0 
   #inserir infos do servidor
   servidor = smtplib.SMTP(HOST, PORTA)
   

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
         enviar_email(anivers)
      else:
         print("Opcao invalida. Opcao desconhecida")
         

