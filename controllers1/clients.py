from calendar import isleap
from datetime import date
import datetime
import shutil
import tempfile
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

   def eh_ano_bissexto(self):
        ano_atual = datetime.now().year
        return isleap(ano_atual) == False
    
   def faz_aniversario_ano_bissexto(self):
        dia, mes = self.data_nascimento
        return dia == "29" and mes == "02"

   def get_dia_mes_aniversario(self) -> dict["dia": str, "mes": str, "ano": str]:
        dia, mes = self.data_nascimento.split("/")[:2]

        if self.eh_ano_bissexto() and self.faz_aniversario_ano_bissexto():
            dia = "28"

        data = {
            "dia": int(dia),
            "mes": int(mes)
        }
        return data   

  
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



def get_todos_clientes():
 with open('clientes.csv', 'r', encoding='utf8') as arquivo_csv:
     reader = csv.DictReader(arquivo_csv)
     for row in reader:
        nome = row["nome_completo"]
        email = row["email"]
        print(f"Nome: {nome}, Email: {email}")
 
get_todos_clientes()
     

def get_mostrar_aniver():
    hoje = date.today()
    aniversariantes = []

    with open('clientes.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data_nascimento = date.fromisoformat(row['data_nascimento'])
            nome = row["nome_completo"]
            if data_nascimento.day == hoje.day and data_nascimento.month == hoje.month:
                aniversariantes.append(row['nome_completo'])
            
            else:
               print("Não existe na data de hoje nenhum cliente fazendo aniver")

            return aniversariantes

get_mostrar_aniver()


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
               print(" Esse mês é aniver do cliente): " , aniver)
      else:
         print("Nao há aniversariantes esse mes")


def editar_clientes(nome_completo):
   cliente = get_nome(nome_completo)
   with open("clientes.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
   
   if cliente in rows:
      print("Cliente encontrado com sucesso")
      print(f"Nome: {nome_completo}")
      print(f"Data de nascimento: {cliente['data_nascimento']}")
      print(f"Email: {cliente['email']}") 
      print(f"Data de criacao: {cliente['data_criacao']}")

      while True:
       print("Deseja alterar os dados de email? Se sim digite: 1 se deseja excluir digite: 2, agora se deseja cancelar digite:3  ")
       opcao = input("Digite uma das opcoes")
       if opcao.lower()=="1":
         novo_email = input("Digite o novo email: ")
         cliente['email'] = novo_email
         with open("clientes.csv" , 'w') as csv_file:
           fieldnames = ["nome_completo","data_nascimento","email","data_criacao" ]
           writer = csv.DictWriter(csv_file , fieldnames=fieldnames)
           writer.writeheader
           writer.writerow(cliente)
           print("Email alterado com sucesso")
      
       elif opcao.lower()=="2":
          with open('clientes.csv','r') as csv_file, tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
             reader = csv.DictReader(csv_file)
             fieldnames = reader.fieldnames
            # rows = [row for row in reader if row["nome_completo"] != nome_completo]
             writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
             writer.writeheader()

             for row in reader:
                if row["nome_completo"] != nome_completo:
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


          


           





#TO do excluir_clientes
         

   
    
        
     
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


   