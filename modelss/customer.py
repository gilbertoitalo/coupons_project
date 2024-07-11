from calendar import isleap
from datetime import datetime
from os import getenv
from pipes import Template



class Customer():
   def __init__(self,full_name,birth_date,email,creation_date):
      self.full_name = full_name
      self.birth_date = birth_date
      self.email = email
      self.data_criacao = creation_date


   def is_leap_year(self):
        year = int(self.birth_date.split('/')[-1])
        return isleap(year) == False
    
   def has_leap_year_birthday(self):
        day, month = self.birth_date.split("/")[:2]
        return day == "29" and month == "02"
   
   def get_birthday_day_month(self) -> dict["day": str, "month": str, "year": str]:
        dia, month = self.birth_date.split("/")[:2]

        if not self.is_leap_year() and self.has_leap_year_birthday():
            day = "28"

        date_info = {
            "day": int(day),
            "month": int(month)
        }
        return date_info 
   
   def email_object(self):
        first_name = self.full_name.split(" ")[0]
        
        with open("template_email.txt", "r", encoding="utf8") as template_file:
            email_template = Template(template_file.read())

        content = email_template.substitute(
            NAME=first_name, 
            COMPANY_NAME="SERASA",
            COUPON="TESTE10"
        )
        return {
            "email": self.email,
            "message": content,
            "email_subject": f"Happy Birthday, {first_name}"
        }
   
   @staticmethod
   def show_customers(customers: list) -> None:
        for customer in customers:
            print(f"NAME: {customer.full_name}\nBIRTH DATE: {customer.birth_date}\nEMAIL: {customer.email}\nCREATION DATE: {customer.creation_date}\n")
