#CREATE BY MAYSAM ENAYAT
#----------[NAME]----------#
import os,time,requests
#----------[basic colors]----------#
green="\033[1;32m";red="\033[1;31m";reset="\033[0m"
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '{RED}'
H = '{GREEN}'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
yy = '\033[1;97m'
s="\033[0m"
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' # PUTIH
G = '{GREEN}' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
HBF = '{ HBF }'
#----------[main logo]----------#
def logo():
 os.system("clear");print(f'''{reset}
       ____    ____  _______     ____  ____  
       |_   \  /   _||_   __ \   |_  _||_  _| 
         |   \/   |    | |__) |    \ \  / /   
         | |\  /| |    |  __ /      > `' <    
        _| |_\/_| |_  _| |  \ \_  _/ /'`\ \_  
       |_____||_____||____| |___||____||____| \033[1m \033[1;30mA\033[1;31mF\033[1;32mG \033[0m 

======================================================
[{RED}•{WHITE}] AUTHOR     :{GREEN} MAYSAM ENAYAT{WHITE}
[{RED}•{WHITE}] FACEBOOK   : {BLUE}MAYSAM ENAYAT{WHITE}
[{RED}•{WHITE}] GITHUB     : {ORANGE}MRMAYSAM{WHITE}
[{RED}•{WHITE}] TEAM       : {RED}M — F {WHITE}
[{RED}•{WHITE}] STATUS     : {BLACK}VIP{WHITE}
[{RED}•{WHITE}] VERSION    : 1.{WHITE}
======================================================
[{lg}√{A}] {BB} MRX UNBLOCKER\33[0;m{A}
======================================================''')
def ip():
 ip = requests.get("https://api.ipify.org").text
 logo()
 print(f"\n [{red}•{reset}{GREEN}] USE AIRPLANE MODE FOR 5 SEC BEFORE USE . ") 
 input(f" [{red}•{reset}{red}] PRESS ENTER TO START ... ") 
 print(50*'\033[1;97m-')
 print(f" [{red}•{reset}] DETECTING YOUR IP ADDRESS ... ");time.sleep(3)
 print(f" [{red}•{reset}]{green} YOUR IP ADDRESS : {ip} ")
 print(f" {reset}[{red}•{reset}]{green} TRYING TO UNBLOCK YOUR IP ... ");time.sleep(3)
 print(f" {reset}[{green}✓{reset}]{green} YOUR IP UNBLOCK SUCCESSFULLY \n\n ")
 exit() 
ip()