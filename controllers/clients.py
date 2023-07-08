from datetime import date
from tabulate import tabulate
import csv
import random
from faker import Faker
from dateutil.relativedelta import relativedelta

fake = Faker()

# Gerar dados aleatórios para 100 clientes
dados_clientes = []
for _ in range(50):
    nome_completo = fake.name()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)
    email = fake.email()
    
    # Calcular a data de cricao -2 anos a partir da data atual  
    # Para fazer: preciso trocar a data para uma logica aleatoria
    data_atual = date.today() 
    data_criacao = data_atual + relativedelta (days=random.randint(0, 365*2)) - relativedelta(years=2)


    
    dados_clientes.append([nome_completo, data_nascimento, email, data_criacao])

# Escrever os dados no arquivo CSV
with open('clientes.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['nome_completo', 'data_nascimento', 'email', 'data_criacao'])
    writer.writerows(dados_clientes)

   # print("Arquivo CSV gerado com sucesso!")



def mostrar_todos_clientes():
 with open('clientes.csv', 'r') as arquivo_csv:
     reader = csv.reader(arquivo_csv)
     for linha in reader:
        print(linha)

def mostrar_por_aniver():
   hoje = date.today()
   anivers = []

   with open('clientes.csv' , 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
         data_nascimento = date.fromisoformat(row['data_nascimento'])

      if data_nascimento == hoje.day and data_nascimento == hoje.month: 
        anivers.append(row['name'])

      if anivers:
         for name in anivers:
            print("Hoje é aniver do cliente:" , name)
      else:
         print("Nao existe na data de hoje nenhum cliente fazendo aniversario")

mostrar_por_aniver()  

def mostrar_por_mes(mes_especifico):
   
   aniver_do_mes = []
  
   with open('clientes.csv' , 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
         data_nascimento = date.fromisoformat(row['data_nascimento'])

         if data_nascimento == mes_especifico:
            aniver_do_mes.append(row['name'])
      
         if aniver_do_mes:
            for aniver in aniver_do_mes:
               print("Hoje é aniver do cliente: " , aniver)
      else:
         print("Nao há aniversariantes esse mes")




        

         

   
      #if data_nascimento != hoje.day and data_nascimento != hoje.month: 
       # print("Não existe na data de hoje nenhum cliente fazendo aniversario")
        
     
# Define as colunas da tabela, correspondendo aos campos dos clientes:
  #  headers = ["nome ", "data_nascimento", "email", "cliente_desde"]

# Cria uma lista vazia pra armazenar as linhas de dados da tabela
  #  rows = []

# loop para percorrer a lista de clientes para cada cliente
 #   for cliente in clients:
   #  nome = cliente["nome"]
   #  data_nascimento = cliente["data_nascimento"]
   #  email = cliente["email"]
   #  cliente_desde = cliente["cliente_desde"]
   #  row = [nome, data_nascimento, email, cliente_desde]
   #  rows.append(row)

    # Uso a funcao para formatar os dados e criar a tabela
#  table = tabulate(rows, headers,tablefmt="grid")

  #  print(table)


    