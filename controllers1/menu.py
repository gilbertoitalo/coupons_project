from controllers1 import clients 
 

def iniciar_menu_principal():
    while True:
        print("1 - Consultar clientes\n2 - Cadastrar cliente\n3 - Editar Clientes" 
              "\n4 - Enviar cupons via email aos clientes aniversariantes\n5 - Sair")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':
                
                iniciar_submenu_consulta_clientes()
            case '2':
                print("Olá vamos cadastrar um cliente")
                nome = input(("Digite o nome e sobrenome: \n"))
                data_nascimento = input("Digite a  data de nascimento. conforme o exemplo ex:AAAA-MM-DD: \n")
                email = input("Digite o email: \n")
                # TO DO implementar para data de criacao o date.now 
                data_criacao = input("Digite a data de hoje, como no exemplo AAAA-MM-DD: \n")
                cliente = clients.Cliente(nome,data_nascimento,email,data_criacao)
                cliente.cadastrar_clientes()
                
                clients.Cliente.cadastrar_clientes
                clients.__name__ = input()
            case '3':
                nome_completo = input( "Olá confirme os dados do cliente, digite o nome completo: ")
                clients.editar_clientes(nome_completo)
            case '4':
                print("ENVIAR CUPONS VIA EMAIL")
            case '5':
                break
            case other:
                print("Opção inválida")

def iniciar_submenu_consulta_clientes():
    while True:
        print("1 - Todos\n2 - Aniversariantes\n3 - Aniversariantes de um mês específico\n4 - Voltar para o menu principal")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':
                 clients.get_todos_clientes()
                 
                 
            case '2':
                clients.get_mostrar_aniver()
                
            case '3':
                mmes_especifico =input("Digite o mes e ano que gostaria de pesquisar")
                clients.mostrar_por_mes(mmes_especifico)
                break
            case '4':
                break
            case other:
                print("Opção inválida")

iniciar_menu_principal()