import webbrowser
webbrowser.open('https://t.me/M_A_M_ll')
import os,sys,subprocess,webbrowser 
subprocess.getoutput("pip install mechanize")
import requests,sys,os,time
import pyfiglet
import requests 
import random 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
insta="_qwertyuiopasdfghjklzxcvbnm1234567890"
ajw="_."
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
#------------------logo---------------------#
print(f'''\033[2;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALRAES Tools
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM		
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mMY NAME     : ALRAES 👑
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mTELEGRAM    : @M_A_M_ll
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mTOOL        : ALRAES ¦¦ 𝗣𝗬𝗧𝗛𝗢𝗡 المدفوعة 
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mTELEGRAM    : @CC8CD
\033[2;35m\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
#------------------------- logo ---------------------------#
id = "7540870238"
token = "8895448772:AAGPdfN1mqV1UcMnRBxmC0Z3DZbk8UUtztw"

def instaa(user):
    
    url_check = f'https://www.instagram.com/{user}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    try:
        response = requests.get(url_check, headers=headers, timeout=10)
        if response.status_code == 404:
            
            email=0
            print(W+f" » {C} Hit user ~> {F}{user} ")
            email+=1
            god=f"""𖤍 اب نيو الريس جابلك يوزر تفضل  𖤍▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
        ALRAES <•••> @{user}
        ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭  
        Tele ~> @M_A_M_ll <•••> @CC8CD"""
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
        else:
            
            print(W+f" »{F} Not user ~> {C}{user} ")
    except Exception as e:
        
        print(W+f" » {Z} Error checking » {A}{user} ")

def users():
    ran1="1234567890qwertyuiopasdfghjklzxvcbnm"
    while True:
        v1 = str(''.join((random.choice(insta) for i in range(1))))
        v2 = str(''.join((random.choice(ajw) for i in range(1))))
        v3 = str(''.join((random.choice(insta) for i in range(1))))
        v4 = str(''.join((random.choice(ajw) for i in range(1))))
        v5 = str(''.join((random.choice(insta) for i in range(1))))
        user1 = (v5+v1+v2+v3+v4)
        user2 = (v1+v5+v2+v3+v4)
        user3 = (v1+v2+v5+v3+v4)
        user4 = (v1+v2+v3+v4+v5)
        ajwad= (user1, user2, user3 ,user4)
        user = random.choice(ajwad)
        instaa(user)
    
        time.sleep(0.5)
users()
