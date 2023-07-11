from datetime import date
from tabulate import tabulate
import csv
import random
from faker import Faker
from dateutil.relativedelta import relativedelta

fake = Faker()

class Cliente:
   def __init__(self,nome_completo,data_nascimento,email,data_criacao) -> None:
      self.nome = nome_completo
      self.data_nascimento = data_nascimento
      self.email = email
      self.data_criacao = data_criacao

   def cadastrar_clientes(self):
      with open('clientes.csv','a') as clientes_csv:
         writer = csv.writer(clientes_csv)
         writer.writerow([self.nome, self.data_nascimento,self.email, self.data_criacao])   
   
      print( f"Cliente," +{self.nome} +"cadastrado com sucesso")

  
# Gerar dados aleatórios para 50 clientes
#dados_clientes = []
#or _ in range(50):
   # nome = fake.name()
   # data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)
   # email = fake.email()
    
    # Calcular a data de cricao -2 anos a partir da data atual  
    # Para fazer: preciso trocar a data para uma logica aleatoria
    #data_atual = date.today() 
    #data_criacao = data_atual + relativedelta (days=random.randint(0, 365*2)) - relativedelta(years=2)


    
    #dados_clientes.append([nome, data_nascimento, email, data_criacao])

# Escrever os dados no arquivo CSV
#with open('clientes.csv', 'w', encoding="utf8") as arquivo_csv:
   # writer = csv.writer(arquivo_csv)
    #writer.writerow(['nome_completo', 'data_nascimento', 'email', 'data_criacao'])
    #writer.writerows(dados_clientes)

   # print("Arquivo CSV gerado com sucesso!")



def mostrar_todos_clientes():
 with open('clientes.csv', 'r', encoding='utf8') as arquivo_csv:
     reader = csv.DictReader(arquivo_csv)
     for row in reader:
        nome = row["nome_completo"]
        email = row["email"]
        print(f"Nome: {nome}, Email: {email}")
 
mostrar_todos_clientes()
     

def mostrar_por_aniver():
    hoje = date.today()
    aniversariantes = []

    with open('clientes.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data_nascimento = date.fromisoformat(row['data_nascimento'])
            nome = row["nome_completo"]
            if data_nascimento.day == hoje.day and data_nascimento.month == hoje.month:
                aniversariantes.append(row['nome_completo'])

            return aniversariantes

mostrar_por_aniver()


#To do: criar uma vreficacao caso cliente nascer em ano bissexto 
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


def editar_clientes(nome, data_nascimento, email):
   with open("clientes.csv" , "r") as csv_file:
      reader = csv.DictReader(csv_file)
      rows = list(reader)

   for row in rows:
      if row ["nome"] == nome:
         row ["data_nascimento"] == data_nascimento
         row ["email"] == email

   with open("clientes.csv" , 'w') as csv_file:
     fieldnames = ["nome","data_nascimento" , "email","data_criacao"]
     writer2 = csv.DictWriter(csv_file , fieldnames=fieldnames)
     writer2.writeheader
     writer2.writerows(rows)


#TO do excluir_clientes
         

   
    
        
     
# TO DO a fuction to apply the coupons 

def get_nome(nome):
   with open('clientes.csv' 'r ') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
         if row["wmIL"] == nome:
            return row["nome completo"]
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



   