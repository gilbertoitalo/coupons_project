from controllers import clients

def iniciar_menu_principal():
    while True:
        print("1 - Consultar clientes\n2 - Cadastrar cliente\n3 - Editar Clientes" 
              "\n4 - Enviar cupons via email aos clientes aniversariantes\n5 - Sair")
        opcao_escolhida = input("Digite uma opção: ")

        match opcao_escolhida:
            case '1':
                
                iniciar_submenu_consulta_clientes()
            case '2':
                print("CADASTRAR CLIENTE") 
            case '3':
                print("Editar Clientes")
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
                
                clients.csv

            
            case '2':
                print("CONSULTAR CLIENTES ANIVERSARIANTES")
                break
            case '3':
                print("CONSULTAR CLIENTES ANIVERSARIANTES DE UM MÊS ESPECÍFICO")
                break
            case '4':
                break
            case other:
                print("Opção inválida")

iniciar_menu_principal()