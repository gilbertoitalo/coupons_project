from calendar import isleap
from datetime import datetime


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
   
   @staticmethod
   def mostrar_clientes(clientes: list) -> None:
        for cliente in clientes:
            print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}\n")
