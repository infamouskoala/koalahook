import threading
import requests
from pystyle import Colors, Colorate, Center
import time
import os
import webbrowser
import base64
from tkinter import filedialog as fd
# Removed: from webhook import WEBHOOK

# ----------------------------
# New: Webhook file management
WEBHOOK_FILE = "webhook.txt"

def save_webhook(url: str):
    with open(WEBHOOK_FILE, "w") as f:
        f.write(url.strip())

def load_webhook() -> str:
    if os.path.exists(WEBHOOK_FILE):
        with open(WEBHOOK_FILE, "r") as f:
            url = f.read().strip()
            if url:
                return url
    # If file missing or empty, ask user for webhook url
    url = input("Enter your webhook URL: ").strip()
    save_webhook(url)
    return url

def clear_webhook():
    save_webhook("")  # Overwrite with empty string
# ----------------------------

# colors because I cannot remember to change it everytime

black = "\033[1;30m"
titletext = " [-- KOALAHOOK --] Made by github.com/infamouskoala"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[! KOALAHOOK !]{white} Invalid url!"
# test = "" test webhook, dont forget to remove :3

socials = {
    "github": {"link": "https://github.com/infamouskoala"},
    "youtube": {"link": "https://youtube.com/infamouskoala"},
}  # You can update this list, and it will dynamically update.

logo = """
      __   __)             ____  ___)        
     (, ) /         /)    (, /   /        /) 
        /(   ____   // _     /---/  ______(/_ 
     ) /  \_(_)(_(_(/_(_(_) /   (__(_)(_) /(__
    (_/                  (_/                  
    >> [Webhook Multitool developed by @infamouskoala]
"""

for platform, info in socials.items():
    link = info["link"].replace("https://", "")
    logo += f"      > [{platform.capitalize()}]: {link}\n"

logo = Center.XCenter(logo)


def choice():
    print(Center.XCenter("""\
[1] Send Message
[2] Delete Webhook
[3] Rename Webhook
[4] Spam Webhook
[5] Webhook Information
[6] Log Out
[7] Change pfp
[0] Source Code
"""))


def printascii():
    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(text: str = None):
    if text:
        print(text)
    os.system('pause >nul' if os.name == 'nt' else 'read -n 1 -s -r -p ""')


def intromenu():
    clear()
    printascii()
    choice()


def changepfp(url):
    input(f"{yellow}[? KOALAHOOK ?]{white} Press enter to select file or skip this to input the path/url")
    image_path = fd.askopenfilename(filetypes=[("Profile Pictures", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        clear()
        image_path = input(f"{yellow}[? KOALAHOOK ?]{white} Path/URL to image: ")

    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "avatar": f"data:image/jpeg;base64,{encoded_image}"
        }
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Profile picture changed successfully.")
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Error: {e}")


def deletehook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to delete webhook...")
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Webhook deleted successfully.")
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Error: {e}")


def sendmessage(url):
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Message: ")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Message sent successfully.")
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Error: {e}")


def renamehook(url):
    name = input(f"{yellow}[? KOALAHOOK ?]{white} Webhook Name: ")
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to change username...")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Webhook name changed successfully.")
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Error: {e}")


def spamhook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to spam webhook...")
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Spam Text: ")
    timeout = float(input(f"{yellow}[? KOALAHOOK ?]{white} Timeout (to avoid API rate-limit): "))
    try:
        print(f"{red}[! KOALAHOOK !] Spam has started. Relaunch the tool to stop spam.")
        while True:
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{green}[+ KOALAHOOK +]{white} Sent message")
            time.sleep(timeout)
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Error: {e}")


# Anti-skid message
with open(f"{os.getcwd()}\\src\\skidded.txt", "w+", encoding="utf-8") as file:
    content = "Greetings user, this file has been originally developed by Infamous Koala. You can find him here:\n"
    for platform, info in socials.items():
        content += f"{info['link']}\n"
    content += """\n\nIf this tool was sold to you, you got scammed — it's free on GitHub and YouTube.
Read the license and terms before using.

- Infamous Koala
"""
    file.write(content)

os.system("title github.com/infamouskoala")

# Display intro once
clear()
printascii()
print(Center.XCenter(f"{cyan}Loading KOALAHOOK..."))
time.sleep(1.5)

# MAIN LOOP
while True:
    clear()
    printascii()
    try:
        url = load_webhook()  # <- load webhook from file or input
        response = requests.get(url)
        if response.status_code == 200:
            webhook = response.json()
        else:
            print(f"[{response.status_code}]: Invalid Webhook")
            pause("Press any key to exit...")
            raise SystemExit
    except Exception as e:
        print(f"{red}[! KOALAHOOK !] Failed to connect to webhook: {e}")
        pause("Press any key to exit...")
        raise SystemExit

    while True:
        intromenu()
        webhook_name = webhook["name"]
        print(f"\n\n\n{green}[+ KOALAHOOK +]{white} Logged into webhook: {webhook_name}")
        try:
            ch = int(input(f"{cyan}[>]{white} --> "))
        except ValueError:
            print(f"{red}[! KOALAHOOK !] Invalid input, please enter a number.")
            pause("Press any key to return to menu...")
            continue

        if ch == 1:
            clear()
            sendmessage(url)
            pause("Press any key to return to menu...")
        elif ch == 2:
            clear()
            deletehook(url)
            pause("Press any key to return to menu...")
        elif ch == 3:
            clear()
            renamehook(url)
            pause("Press any key to return to menu...")
        elif ch == 4:
            clear()
            spamhook(url)
            pause("Press any key to return to menu...")
        elif ch == 5:
            print("\nWebhook Information:")
            print("    Webhook ID:", webhook["id"])
            print("    Name:", webhook["name"])
            print("    Type:", webhook["type"])
            print("    Token:", webhook["token"])
            if webhook.get("application_id"):
                print("    Application ID:", webhook["application_id"])
            print("    Guild ID:", webhook.get("guild_id"))
            print("    Channel ID:", webhook.get("channel_id"))
            if "user" in webhook:
                user = webhook["user"]
                print("Creator Info: {}#{} (ID: {})".format(user["username"], user["discriminator"], user["id"]))
            pause("\nPress any key to return to menu...")
        elif ch == 6:
            # Clear the saved webhook on logout
            clear_webhook()
            os.system("title Logging out...")
            print("Logging out, please wait...")
            break
        elif ch == 7:
            clear()
            changepfp(url)
            pause("Press any key to return to menu...")
        elif ch == 0:
            print(f"{cyan}[+ KOALAHOOK +]{white} Source code can be found here:")
            for platform, info in socials.items():
                link = info["link"].replace("https://", "")
                print(f"{platform.capitalize()}: {link}")
            while True:
                name = input("Enter the platform name to open it (or 'exit'): ").lower()
                if name == 'exit':
                    break
                if name in socials:
                    link = socials[name]["link"]
                    open_link = input(f"Open {name}? [y/n]: ").lower()
                    if open_link == "y":
                        webbrowser.open(link)
                else:
                    print("Unknown platform.")
