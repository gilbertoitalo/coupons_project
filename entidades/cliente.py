from calendar import isleap
from datetime import datetime
from os import getenv
from pipes import Template



class Cliente():
   def __init__(self,nome_completo,data_nascimento,email,data_criacao):
      self.nome_completo = nome_completo
      self.data_nascimento = data_nascimento
      self.email = email
      self.data_criacao = data_criacao


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
   
   def objetc_email(self):
        primeiro_nome = self.nome_completo.split(" ")[0]
        
        with open(("template_email.txt"), "r", encoding="utf8") as arquivo_template:
            template_email = Template(arquivo_template.read())

        conteudo = template_email.substitute(
            NOME=primeiro_nome, 
            NOME_EMPRESA=("SERASA"),
            CUPOM="TESTE10"
        )
        return {
            "email": self.email,
            "mensagem": conteudo,
            "titulo_email": f"Feliz aniversário, {primeiro_nome}"
        }
   
   @staticmethod
   def mostrar_clientes(clientes: list) -> None:
        for cliente in clientes:
            print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}\n")
