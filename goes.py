import os 
import webbrowser
import time


#this is the logo function 
def logo(): 

    print('''
.------..------..------..------.
|G.--. ||O.--. ||E.--. ||S.--. |
| :/\: || :/\: || (\/) || :/\: |
| :\/: || :\/: || :\/: || :\/: |
| '--'G|| '--'O|| '--'E|| '--'S|
`------'`------'`------'`------'
        ''')

# this is the clear function   
def clear():
    if os.name == 'posix': 
        _ =  os.system('clear')
    elif os.name == 'nt': 
        _ = os.system('cls')

# this is the done fuction 
def Done():
   print('''
██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝                                
         ''')




#this is the url 
url = "https://nos.nl/"

#this is the function that makes so if you load the function it opens 
def open():
 webbrowser.open(url)




           
# this loads the logo function 
logo()
time.sleep(4)
clear()
# this opens the url and sends done
open()
Done()