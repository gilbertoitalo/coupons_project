import views.menu as menu 
from datetime import datetime



if __name__ == "main":
 print(f"\n{datetime.now().strftime('%d/%m/%y, %H:%M:%S')}\n")
 menu.main_menu()

