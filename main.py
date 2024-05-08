import colorama
import shutil
import json
import os
from colorama import Fore
from Widevine import *
from bs4 import BeautifulSoup

# Coded By ENG/ Mohamed Sami Elhamzawy
# Facebook ---> https://web.facebook.com/MoSami.74
# Linkedin ---> https://www.linkedin.com/in/mohamed-elhamzawy-1b862b273/

colorama.init()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "\n" + "Widevine Keys Tool (Coded By Mohamed S. ElHamzawy)".center(shutil.get_terminal_size().columns) + "\n")
    print(f"{Fore.RED}Total keys count : {Fore.GREEN}{Widevine.CountKeys()} \n")

MainMenu_Id = 0

def Starting():
    global MainMenu_Id
    
    print(Fore.GREEN , f"Main Menu: \n 1: Send a request \n 2: Get key \n 3: Get PSSH \n 4: Exit \n")
    MainMenu_Id = int(input(f"{Fore.RED}Please choose an option from the main menu: {Fore.GREEN}"))
    clear_terminal()
    if MainMenu_Id == 1:    
        Pssh = input(f"{Fore.RED}Input PSSH : {Fore.GREEN}")
        License = input(f"{Fore.RED}Input License : {Fore.GREEN}")
        Headers = input(f"{Fore.RED}Input Headers : {Fore.GREEN}")
        Build_Info = input(f"{Fore.RED}Input Build Info : {Fore.GREEN}")
        Proxy = input(f"{Fore.RED}Input Proxy : {Fore.GREEN}")
        Cache = input(f"{Fore.RED}Input Cache (Yes / No) : {Fore.GREEN}")
        print("\n")
        CK_Request = Widevine.RequestCK(pssh = Pssh ,license = License ,Headers = Widevine.convert_headers(Headers) ,buildInfo = Build_Info, proxy = Proxy, cache = Cache)
        soup = BeautifulSoup(CK_Request, 'html.parser')
        li_elements = soup.find_all('li', style="font-family:'Courier'")
        extracted_strings = [li.get_text() for li in li_elements]
        i = 1
        for string in extracted_strings:
            print(f"{Fore.RED}{i}. {Fore.GREEN}{string}")
            i += 1   
            
        print(Fore.GREEN , f"\n1: Back to main menu \n2: Send another Request \n3: Exit \n")
        MainMenu_Id2 = int(input(f"{Fore.RED}Please choose an option from the menu: {Fore.GREEN}"))
        
    elif MainMenu_Id == 2:
        MainMenu_Id2 = 0
        while MainMenu_Id2 !=3 :
            KID_PSSH = input(f"{Fore.RED}Input PSSH/KID : {Fore.GREEN}")
            ck = Widevine(KID_PSSH)
            data = json.loads(ck.GetCK())
        
            if "error" in data:
                print(f"{Fore.RED}Error : {Fore.GREEN}{data['error']}")
            else:
                print("\n")
                print(f"{Fore.RED}Time : {Fore.GREEN}{data['time']} \n")
                i = 1
                for keys in data['keys']:
                    print(f"{Fore.RED}{i}. {Fore.GREEN}{keys['key']}")
                    i += 1
                print(Fore.GREEN , f"\n1: Back to main menu \n2: Get another key \n3: Exit \n")
                MainMenu_Id2 = int(input(f"{Fore.RED}Please choose an option from the menu: {Fore.GREEN}"))
                if MainMenu_Id2 == 1:
                    MainMenu_Id = 0
                    break;
                elif MainMenu_Id2 == 2:
                    clear_terminal()
                    MainMenu_Id = 2
                elif MainMenu_Id2 == 3:
                    MainMenu_Id = 4
                    break;
    elif MainMenu_Id == 3:
        MainMenu_Id3 = 0
        while MainMenu_Id3 !=3 :
            Pssh = Widevine.GetPSSH(input(f"{Fore.RED}Input URL : {Fore.GREEN}"))

            soup = BeautifulSoup(Pssh, "xml")
            cenc_pssh_tags = soup.find_all("cenc:pssh")
            base64_strings = [tag.text for tag in cenc_pssh_tags]
            pssg_len = float('inf')
            pssh_string = ""
            for str_pssh in base64_strings:
                if len(str_pssh) < pssg_len:
                    pssg_len = len(str_pssh)
                    pssh_string = str_pssh
                    
            print(f"\n{Fore.RED}PSSH :")
            print(f"{Fore.GREEN}{pssh_string}")
            
            print(Fore.GREEN , f"\n1: Back to main menu \n2: Get another PSSH \n3: Exit \n")
            MainMenu_Id3 = int(input(f"{Fore.RED}Please choose an option from the menu: {Fore.GREEN}"))
            
            if MainMenu_Id3 == 1:
                MainMenu_Id = 0
                break;
            elif MainMenu_Id3 == 2:
                clear_terminal()
                MainMenu_Id = 3
            elif MainMenu_Id3 == 3:
                MainMenu_Id = 4
                break;
  
while MainMenu_Id != 4:
    clear_terminal()
    Starting()
os.system('cls' if os.name == 'nt' else 'clear')