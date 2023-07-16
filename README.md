Documentação do Projeto de Envio de Cupons para Clientes Aniversariantes

Visão Geral do Projeto
 O Projeto de Envio de Cupons para Clientes Aniversariantes tem como objetivo automatizar o envio de cupons de desconto para clientes que estão comemorando seus aniversários. O sistema permite consultar clientes, cadastrar novos clientes, enviar cupons de desconto via e-mail e apresentar os dados dos clientes de forma organizada.


Requistos 

REQ 01: Menu de Navegação
O sistema deve fornecer um menu de navegação com as seguintes opções:
1) Consultar clientes
2) Cadastrar cliente
3) Editar cliente
4) Enviar cupons via e-mail aos clientes aniversariantes
5) Sair

### REQ 02: Submenu de Filtros para Consulta de Clientes
Ao selecionar a opção "Consultar clientes" no menu, o sistema deve fornecer um submenu com opções de filtros:
1) Todos
2) Aniversariantes
3) Aniversariantes de um mês específico
4) Voltar ao menu principal

### REQ 03: Apresentação dos Dados em Tabela
Os dados dos clientes consultados devem ser apresentados em formato de tabela, com as seguintes colunas:
- NOME COMPLETO
- DATA DE NASCIMENTO
- E-MAIL
- CLIENTE DESDE

### REQ 04: Cadastro de Novo Cliente
O sistema deve permitir o cadastro de um novo cliente, com as seguintes informações:
- Nome completo
- Data de nascimento
- E-mail
- Data de criação

### REQ 05: Editar ou excluir Cliente 

O sistema deve permitir editar todos os campos de dados do cliente:



Os novos clientes cadastrados devem ser incluídos no arquivo "clientes.csv".

### REQ 06: Envio de E-mails
O sistema deve enviar e-mails aos clientes aniversariantes com um cupom de desconto. O processo de envio de e-mails segue as seguintes etapas:

1) O sistema identifica os clientes aniversariantes cadastrados no arquivo "clientes.csv".
2) O sistema exibe a quantidade de e-mails a serem enviados e pergunta ao usuário se deseja enviar ou ver os destinatários.
3) Se o usuário escolher "ver", o sistema exibe os destinatários em formato de tabela.
4) Se o usuário escolher "enviar", o sistema envia os e-mails aos destinatários com as seguintes informações:
- Título do e-mail: "Feliz aniversário, \<primeiro nome da pessoa>"
- Corpo da mensagem: "Olá, \<primeiro nome>.
Nós da \<nome da loja> te desejamos um feliz aniversário.
Aqui está um cupom de desconto para utilizar nas compras de nossos produtos e serviços:
\<cupom de desconto>"

Regras para gerar o cupom de desconto:
- O cupom deve ter o formato \<PRIMEIRO NOME DO CLIENTE>\<% DESCONTO> (por exemplo, FULANO10 para 10% de desconto).
- O desconto máximo é de 30%.
- A porcentagem de desconto é calculada de acordo com a data de criação da conta do cliente:
  - Até 1 ano: 10%
  - De 1 ano até 2 anos: 20%
  - De 2 anos ou mais: 30%

## Execução do Projeto
Para executar o projeto, siga as etapas abaixo:

1) Clone o repositório do projeto do GitHub.
2) Certifique-se de ter as dependências necessárias instaladas.
3) Execute o arquivo principal do projeto para iniciar a aplicação.
4) Utilize o menu de navegação para consultar clientes, cadastrar um novo cliente ou enviar cupons via e-mail aos clientes aniversariantes.

## Considerações Finais
A documentação acima fornece uma visão geral do projeto de Envio de Cupons para Clientes Aniversariantes, incluindo requisitos e informações sobre o funcionamento do sistema. Siga as instruções fornecidas para executar o projeto corretamente. .

