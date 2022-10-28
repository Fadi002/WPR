import os,subprocess
os.system('cls')
os.system('@echo off')
os.system('title Windows Password Removal by fadi')
banner = '''\033[31m
                            .oodMMMM
                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM                    Windows Password Removal by fadi
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM                    https://github.com/Fadi002/WPR
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
				    
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM
type !help to print all commands
'''
def help():
      print('''
!help - show this menu
!restart - restart the pc
!poweroff - shutdown the pc
!change_password - change user account password
!remove_password - remove user account password
!clear - clear the console
!shell - open cmd here
!exit - close the toolkit
''')

def clear():
      os.system('cls')
      print(banner)
clear()
def remove_password():
      userr = input('Enter account username : ')
      try:
            idk = subprocess.check_output(f"net users {userr}", shell=True, universal_newlines=True)
            os.system(f'echo | net users {userr} *')
            print('\ndone now just login with empty password or restart')
      except:
            print('error user not found')

def change_password():
      userr = input('Enter account username : ')
      try:
            idk = subprocess.check_output(f"net users {userr}", shell=True, universal_newlines=True)
            os.system(f'net users {userr} *')
            print('\ndone now just login')
      except:
            print('error user not found')
      
while True:
      choice = input('>>> ')
      if choice.startswith('!help'):
            help()
      elif choice.startswith('!clear'):
            clear()
      elif choice.startswith('!shell'):
            os.system('start C:\\Windows\\System32\\cmd.exe')
      elif choice.startswith('!exit'):
            exit(1337)
      elif choice.startswith('!restart'):
            os.system('shutdown /r /t 0')
      elif choice.startswith('!poweroff'):
            os.system('shutdown /s /t 0')
      elif choice.startswith('!change_password'):
            change_password()
      elif choice.startswith('!remove_password'):
            remove_password()