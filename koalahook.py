import threading
import requests
from pystyle import Colors, Colorate, Center
import time
import os
import webbrowser
import base64

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

title_lock = threading.Lock()

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
    print(Center.XCenter("""
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
    os.system(
        'clear' if os.name != 'nt' else 'cls')  # should be a better one-liner, because let's be real if its unsupported they are on some next wacky shit
    # if os.name == 'posix':  # Unix/Linux/MacOS
    #     os.system('clear')
    # elif os.name == 'nt':  # Windows
    #     os.system('cls')
    # else:
    #     print("Unsupported operating system")
    #     raise SystemExit


def pause(text: str = None):
    if text:
        print(text)
    os.system(
        'read -n 1 -s -r -p ""' if os.name != 'nt' else 'pause >nul')  # should be a better one-liner, because let's be real if its unsupported they are on some next wacky shit
    # if os.name == 'posix':  # Unix/Linux/macOS
    #     os.system('read -n 1 -s -r -p ""')
    # elif os.name == 'nt':  # Windows
    #     os.system('pause >nul')
    # else:
    #     print("Unsupported operating system")
    #     raise SystemExit


def intromenu():
    clear()
    printascii()
    choice()
    scrolling_thread = threading.Thread(target=scrolling)
    scrolling_thread.start()

# Options start here

# '''
# # might make this idk or might remove it
# def sendembed(url):
#     tit = input(f"{yellow}[? KOALAHOOK ?]{white}Title for the embed: ")
#     des = input(f"{yellow}[? KOALAHOOK ?]{white}Description: ")
#     color = input(f"{yellow}[? KOALAHOOK ?]{white}Hex-Color: ")
#     colormain = f"0x{color}"
#     embed = discord.Embed(title=tit, description=des, color=colormain)
#     requests.post(url,json={"embed":embed})
# '''


# Updated By JoeV2


def changepfp(url):
    choice = (f"""
{yellow}[1]{white} URL For PFP              
{yellow}[2]{white} Image Path for PFP
              """)
    print(choice)
    pfp_choice = input(f"{yellow}[? KOALAHOOK ?]{white} Choose an option for the profile picture: ")
    
    if pfp_choice == "1":
        image_url = input(f"{yellow}[? KOALAHOOK ?]{white} URL of the image: ")
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        except requests.exceptions.HTTPError as errh:
            print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")
            return
        except requests.exceptions.RequestException as err:
            print(f"{red}[! KOALAHOOK !] Request Exception: {err}")
            return
    elif pfp_choice == "2":
        image_path = input(f"{yellow}[? KOALAHOOK ?]{white} Local path of the image: ")
        try:
            with open(image_path, 'rb') as file:
                encoded_image = base64.b64encode(file.read()).decode('utf-8')
        except FileNotFoundError:
            print(f"{red}[! KOALAHOOK !] Image file not found.")
            return
    else:
        print(f"{red}[! KOALAHOOK !] Invalid choice.")
        return

    data = {
        "avatar": f"data:image/jpeg;base64,{encoded_image}"
    }
    try:
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Profile picture changed successfully.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! KOALAHOOK !] Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{red}[! KOALAHOOK !] Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{red}[! KOALAHOOK !] Request Exception: {err}")




def deletehook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to delete webhook...")
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f"{green}[+ KOALAHOOK +]{white} Webhook deleted successfully.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! KOALAHOOK !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! KOALAHOOK !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! KOALAHOOK !] Request Exception: {err}")

def sendmessage(url):
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Message: ")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Message sent successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! KOALAHOOK !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! KOALAHOOK !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! KOALAHOOK !] Request Exception: {err}")

def renamehook(url):
    name = input(f"{yellow}[? KOALAHOOK ?]{white} Webhook Name: ")
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to change username...")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Webhook name changed successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! KOALAHOOK !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! KOALAHOOK !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! KOALAHOOK !] Request Exception: {err}")

def spamhook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to spam webhook...")
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Spam Text: ")
    timeout = float(input(f"{yellow}[? KOALAHOOK ?]{white} Timeout (to avoid api-ratelimit): "))
    try:
        print(f"{red}[! KOALAHOOK !] Spam has started, Relaunch the tool to stop spam and use it again.")
        while True:
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{green}[+ KOALAHOOK +]{white} Sent message")
            time.sleep(timeout)
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! KOALAHOOK !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! KOALAHOOK !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! KOALAHOOK !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! KOALAHOOK !] Request Exception: {err}")


webhook = {}

def scrolling():
    global titletext
    while True:
        with title_lock:
            os.system(f"title {titletext}")
            time.sleep(0.1)
            titletext = titletext[1:] + titletext[0]

def main():
    while True:
        clear()
        printascii()
        while True:
            try:
                url = input(f"{cyan}[>]{white} url: ")
                response = requests.get(url)
                if response.status_code == 200:
                    webhook = response.json()
                    break
                else:
                    print(f"[{response.status_code}]: Invalid Webhook")
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    raise SystemExit
                print("Invalid Webhook")

        while True:
            intromenu()
            webhook_name = webhook["name"]
            print(f"\n\n\n{green}[+ KOALAHOOK +]{white} Logged into webhook: {webhook_name}")
            ch = int(input(f"{cyan}[>]{white} --> "))

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
                if webhook["application_id"]:
                    print("Application ID: {}".format(webhook["application_id"]))

                print("Server Information\n    Guild ID: {}\n    Channel ID: {}".format(webhook["guild_id"], webhook["channel_id"]))
                print("Webhook Information\n    Webhook ID: {}\n    Name: {}\n    Type: {}\n    Token: {}".format(webhook["id"], webhook["name"], webhook["type"], webhook["token"]))
                user = webhook["user"]
                print("User Information (Creator)\n    Username: {}\n    User ID: {}".format(user["username"] + "#" + user["discriminator"], user["id"]))

                pause("\nPress any key to return to menu...")

            elif ch == 6:
                os.system("title Logging out...")
                print("Logging out, please wait..")
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
                    name = input("Enter the name of the platform you want to open (or 'exit' to quit): ").lower()

                    if name == 'exit':
                        break

                    if name in socials:
                        link = socials[name]["link"]
                        x = input(f"Would you like to open {name.capitalize()} in your browser [y/n]? ").lower()
                        if x == "y":
                            webbrowser.open(link)
                        elif x == "n":
                            pass
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                    else:
                        print("Platform not found. Please enter a valid platform.")

if __name__ == '__main__':
    scrolling_thread = threading.Thread(target=scrolling)
    scrolling_thread.start()
    main()
