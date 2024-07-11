from tkinter import ttk
from modelss.customer import functions
from modelss.customers import *
import services.email_service as emails 
from tkinter import *



def main_menu():
    while True:
        print("1 - View Customers\n2 - Register Customer\n3 - Edit Customers"
              "\n4 - Send Coupons via Email to Birthday Customers\n5 - Exit")
        option = input("Enter an option: ")
        if option == '1':
            customer_query_submenu()
        elif option == '2':
            print("Hello, let's register a customer.")
            full_name = input("Enter full name: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            email = input("Enter email: ")
            creation_date = input("Enter today's date (YYYY-MM-DD): ")
            functions.register_customers(full_name, birth_date, email, creation_date)
        elif option == '3':
            full_name = input("Hello, confirm the customer data, enter the full name: ")
            functions.edit_customers(full_name)
        elif option == '4':
            emails.send_emails()
            break  
        elif option == '5':
            break
        else:
            print("Invalid option")

def customer_query_submenu():
    while True:
        print("1 - All\n2 - Birthdays\n3 - Birthdays in a Specific Month\n4 - Back to Main Menu")
        submenu_option = input("Enter an option: ")
        if submenu_option == '1':
            functions.get_all_customers()
        elif submenu_option == '2':
            client = None
            functions.get_all_birthdays(client)
        elif submenu_option == '3':
            specific_month = input("Enter the month (e.g., 02): ")
            functions.show_by_month(specific_month)
        elif submenu_option == '4':
            break
        else:
            print("Invalid option")



if __name__ == '__main__':
    setup_gui()