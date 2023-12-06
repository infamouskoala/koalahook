import requests
from pystyle import Colors, Colorate
import time
import os

#colors because i cannot remember to change it everytime

black = "\033[1;30m"
titletext = "[-- KOALAHOOK --] Made by github.com/infamouskoala"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"    
invalidurl = f"{red}[! KOALAHOOK !]{white} Invalid url!"
# test = "" testhook, dont forget to remove :3
logo = f"""
                                   __   __)             ____  ___)        
                                  (, ) /         /)    (, /   /        /) 
                                    /(   ____   // _     /---/  ______(/_ 
                                 ) /  \_(_)(_(_(/_(_(_) /   (__(_)(_) /(__
                                (_/                  (_/                  
                              >> [Webhook Multitool Developed by @infamouskoala]
                                  > [github.com/infamouskoala]
                                  > [youtube.com/infamouskoala]"""
def choice():
    print("""
                                    [1] Send Message
                                    [2] Delete Webhook
                                    [3] Rename Webhook
                                    [4] Spam Webhook
                                    [5] Log Out
                                    [6] Source Code
""")

def printascii():
    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))

def clear():     #clear for windows and linux || and add the ascii
    os.system("cls || clear")
    printascii()

def intromenu():
    clear()
    choice()
    os.system(f"title {titletext}")

# Options start here

def deletehook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to delete webhook...")
    try:
        requests.delete(url)
        print()
    except Exception as lmaodead:
        print(invalidurl)

def sendmessage(url):
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Message: ")
    try:
        requests.post(url,json={"content":msg})
    except Exception as deadonceagain:
        print(invalidurl)

'''
# might make this idk or might remove it
def sendembed(url):
    tit = input(f"{yellow}[? KOALAHOOK ?]{white}Title for the embed: ")
    des = input(f"{yellow}[? KOALAHOOK ?]{white}Description: ")
    color = input(f"{yellow}[? KOALAHOOK ?]{white}Hex-Color: ")
    colormain = f"0x{color}"
    embed = discord.Embed(title=tit, description=des, color=colormain)
    requests.post(url,json={"embed":embed})
'''

def renamehook(url):
    name = input(f"{yellow}[? KOALAHOOK ?]{white} Webhook Name: ")
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to change username...")
    try:
        requests.patch(url, json={"name":name})
    except Exception as brokenasslmao:
        print(invalidurl)

def spamhook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to spam webhook...")
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Spam Text: ")
    timeout = float(input(f"{yellow}[? KOALAHOOK ?]{white} Timeout (to avoid api-ratelimit): "))
    try:
        print(f"{red}[! KOALAHOOK !] Spam has started, Relaunch the tool to stop spam and use it again.")
        while True:
            r = requests.post(url,json={"content":msg})
            print(f"{green}[+ KOALAHOOK +] Sent message")
            time.sleep(timeout)
    except Exception as brodidntrunlmao:
        print(invalidurl)

def sourcecode():
    print(f"{cyan}[+ KOALAHOOK +]{white} Source code can be found here:\nhttps://github.com/infamouskoala \nDeveloped by:\nhttps://youtube.com/infamouskoala")

os.system("clear || cls")

# injecting antiskid into your pc, no skidding kid :)
file = open("src/skidded.txt","w")
file.write("Greetings user, this file has been originally developed by Infamous Koala. You can find him here:\nhttps://youtube.com/infamouskoala \nhttps://github.com/infamouskoala\nIf this tool was sold to you, I am sorry to tell you that you got scammed since it is free on my github and the showcase is on my youtube.\nAnd if you're skidding it as we speak, please take some time to read the licenses and terms of the tool.\nRegards\nInfamous Koala")
file.close()

printascii()
webhook = input(f"{cyan}[>]{white} url: ")
while True:
    intromenu()
    print(f"{green}[+ KOALAHOOK +]{white} Logged in webhook")
    ch = int(input(f"{cyan}[>]{white} --> "))
    if ch == 1:
        clear()
        sendmessage(webhook)
        time.sleep(0.5)
    elif ch == 2:
        clear()
        deletehook(webhook)
        time.sleep(0.5)
    elif ch == 3:
        clear()
        renamehook(webhook)
        time.sleep(0.5)
    elif ch == 4:
        clear()
        spamhook(webhook)
    elif ch == 5:
        os.system("title Logging out...")
        print("Logging out, please wait..")
        os.system("py koalahook.py || python koalahook.py || python3 koalahook.py")
        clear()
    elif ch == 6:
        sourcecode()
        input("Press any key to reload")