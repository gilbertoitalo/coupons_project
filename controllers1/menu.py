from entidades.email_service import enviar_emails
from entidades.cliente import Cliente 
import repositorio.clients as funcoes 
 

def iniciar_menu_principal():
    while True:
        print("1 - Consultar clientes\n2 - Cadastrar cliente\n3 - Editar Clientes"
              "\n4 - Enviar cupons via email aos clientes aniversariantes\n5 - Sair")
        opcao_escolhida = input("Digite uma opção: ")
        if opcao_escolhida == '1':
            iniciar_submenu_consulta_clientes()
        elif opcao_escolhida == '2':
            print("Olá, vamos cadastrar um cliente")
            nome_completo = input("Digite o nome e sobrenome: ")
            data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
            email = input("Digite o email: ")
            data_criacao = input("Digite a data de hoje (AAAA-MM-DD): ")
            funcoes.cadastrar_clientes(nome_completo, data_nascimento, email, data_criacao)
        elif opcao_escolhida == '3':
            nome_completo = input("Olá, confirme os dados do cliente, digite o nome completo: ")
            funcoes.editar_clientes(nome_completo)
        elif opcao_escolhida == '4':
            
            anivers = funcoes.get_mostrar_aniver()
            enviar_emails()
            break  
        elif opcao_escolhida == '5':
            break
        else:
            print("Opção inválida")

def iniciar_submenu_consulta_clientes():
    
        print("1 - Todos\n2 - Aniversariantes\n3 - Aniversariantes de um mês específico\n4 - Voltar para o menu principal")
        opcao2 = input("Digite uma opção: ")
        if opcao2 == '1':
            funcoes.get_todos_clientes()
        elif opcao2 == '2':
            funcoes.get_mostrar_aniver()
        elif opcao2 == '3':
            mmes_especifico = input("Digite o mês (exemplo: 02): ")
            funcoes.mostrar_por_mes(mmes_especifico)
            
        
            
        else:
            print("Opção inválida")

iniciar_menu_principal()
