from calendar import isleap
from datetime import date
from datetime import datetime
import shutil
import tempfile
import dotenv
from tabulate import tabulate
import csv
import random
from faker import Faker
from dateutil.relativedelta import relativedelta
from models.cliente import Cliente
import os
fake = Faker()

dotenv.load_dotenv()
CAMINHO_ARQUIVO_DADOS = os.getenv("clientes.csv")


def register_customers(nome_completo, data_nascimento, email, data_criacao):
      
      with open('clientes.csv','a') as file_csv:
         writer = csv.writer(file_csv)
         writer.writerow([nome_completo, data_nascimento, email, data_criacao])   
        
   
      print(f"Cliente {nome_completo} cadastrado com sucesso")

      
def get_all_customers():
    

    with open('clientes.csv', 'r', encoding='utf8') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for row in reader:
         if len(row) >= 4:
            nome_completo = row[0]
            data_nascimento = row[1]
            email = row[2]
            data_criacao = row[3]
            print(f"{nome_completo}, {data_nascimento}, {email},{data_criacao}")
        
   

def get_all_anivers(cliente):
    hoje = datetime.today().date()
    anivers = []
    

    with open('clientes.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for cliente in reader:
            birth_date = datetime.strptime(cliente['data_nascimento'],'%Y-%m-%d').date()
            full_name = cliente["nome_completo"]
            if birth_date.month == hoje.month and birth_date.day == hoje.day:
               anivers.append(full_name)
               
    if anivers:  
      print("Aniversariantes de hoje: ")            
      for full_name in anivers:
       print(full_name)
    else:
      print("Não existe na data de hoje nenhum cliente fazendo aniver")

      return anivers

#get_mostrar_aniver()


#To do: criar uma vreficacao caso cliente nascer em ano bissexto 
def show_by_month(specific_month):
     
   mes, ano = specific_month.split("-")
   
   
   data_especifico = datetime.strptime(specific_month,'%Y-%m').date()
   mes = data_especifico.month
   ano = data_especifico.year
   aniver_do_mes = []
  
   with open('clientes.csv' , 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      for cliente in reader:
         data_nascimento = datetime.strptime(cliente['data_nascimento'],'%Y-%m-%d').date()
         nome_completo = cliente["nome_completo"]
         if  data_nascimento.month == mes:
            aniver_do_mes.append(nome_completo)
      
         if aniver_do_mes:
               print(f" Esse mês é aniver do cliente):{mes}/{ano}:")
               for nome_completo in aniver_do_mes:
                  print(nome_completo)
         else:
           print(f"Nao há aniversariantes esse mes :{mes}/{ano}")
   


def editar_clientes(full_name):
   client = get_nome(full_name)
   with open("clientes.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
   
   if client in rows:
      print("Cliente encontrado com sucesso")
      print(f"Nome: {full_name}")
      print(f"Data de nascimento: {client['data_nascimento']}")
      print(f"Email: {client['email']}") 
      print(f"Data de criacao: {client['data_criacao']}")

      while True:
       print("Deseja alterar os dados de email? Se sim digite: 1 se deseja excluir digite: 2, agora se deseja cancelar digite:3  ")
       option = input("Digite uma das opcoes")
       if option.lower()=="1":
         novo_email = input("Digite o novo email: ")
         client['email'] = novo_email
         with open("clientes.csv" , 'w') as csv_file:
           fieldnames = ["nome_completo","data_nascimento","email","data_criacao" ]
           writer = csv.DictWriter(csv_file , fieldnames=fieldnames)
           writer.writeheader
           writer.writerow(client)
           print("Email alterado com sucesso")
      
       elif option.lower()=="2":
          with open('clientes.csv','r') as csv_file, tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
             reader = csv.DictReader(csv_file)
             fieldnames = reader.fieldnames
            # rows = [row for row in reader if row["nome_completo"] != nome_completo]
             writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
             writer.writeheader()

             for row in reader:
                if row["nome_completo"] != full_name:
                   writer.writerow(row)

          shutil.move(temp_file.name, "clietes.csv")
          print("Cliente excluido com sucessso")
          #with open('clientes.csv','w') as csv_file:
          #   fieldnames = ["nome_completo","data_nascimento","email","data_criacao"]
          #   writer.writeheader()
           #  writer.writerows(rows)   
          #   print("Cliente excluido com sucesso")
      # elif opcao.lower() == "3":
       #   print("alteracao cancelada")   


          


           





         

   
    
        
     
# TO DO a fuction to apply the coupons 

def get_nome(nome_completo):
   with open('clientes.csv', 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
         if row["nome_completo"] == nome_completo:
            return row
   return None
         


def get_cupom(nome, data_criacao):
   nome = get_nome(nome)
   if nome is None:
      return None
   
   primeiro_nome = nome.split[0]
   nome.upper()
   desconto = 0 

   ano_criacao = (date.today() - data_criacao) // 355

   if ano_criacao < 1:
      desconto = 10
   elif ano_criacao >= 1 and ano_criacao < 2:
      desconto = 20
   else:
      desconto = 30

   desconto = min(desconto, 30)

   cupom = f"{primeiro_nome}{desconto}"

   return cupom


   