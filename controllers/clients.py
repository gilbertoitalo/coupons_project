from tabulate import tabulate


clients = [
    {"nome": "Adriano", "data_nascimento": "02-05-1976", 
     "email":"adriano078@hotmail.com", "cliente_desde":"16-09-2018"},
]

def mostrar_clientes():
# Define as colunas da tabela, correspondendo aos campos dos clientes:
    headers = ["nome ", "data_nascimento", "email", "cliente_desde"]

# Cria uma lista vazia pra armazenar as linhas de dados da tabela
    rows = []

# loop para percorrer a lista de clientes para cada cliente
    for cliente in clients:
      nome = cliente["nome"]
      data_nascimento = cliente["data_nascimento"]
      email = cliente["email"]
      cliente_desde = cliente["cliente_desde"]
      row = [nome, data_nascimento, email, cliente_desde]
      rows.append(row)

    # Uso a funcao para formatar os dados e criar a tabela
    table = tabulate(rows, headers,tablefmt="grid")

    print(table)