# Features die fehlen: Computermodus, 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[101m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
form_x1=form_x2=form_x3=form_x4=form_x5=form_x6=form11=form12=form13=form14=form15=form16=form21=form22=form23=form24=form25=form26=form31=form32=form33=form34=form35=form36=form41=form42=form43=form44=form45=form46=form51=form52=form53=form54=form55=form56=form61=form62=form63=form64=form65=form66=form71=form72=form73=form74=form75=form76=form81=form82=form83=form84=form85=form86=form91=form92=form93=form94=form95=form96=("              ")
player=fofo=1
form=""
k=l=j=p=ü=ä=üü=ää=öö=" "
round=aktion_passiert=0   
text=1 #kann zwischen 1 und 6 sein (1 ist Favorit!)(danach: 6,(4),3,)
def change_player(self):
    global player
    global form
    if player==1:
        form="O"
        player+=1
    else:
        form="X"
        player-=1
def print_table(self):
        print("""""
        \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        \t\t\t\t\t\t\t\t\t                  ███╗                     ██████╗                 ██████╗  
        \t\t\t\t\t\t\t\t\t                 ████║                     ╚════██╗                 ╚════██╗    
        \t\t\t\t\t\t\t\t\t                ██╔██║                       ███╔═╝                  █████╔╝    
        \t\t\t\t\t\t\t\t\t                ╚═╝██║                     ██╔══╝                    ╚═══██╗    
        \t\t\t\t\t\t\t\t\t                ███████╗                   ███████╗                 ██████╔╝    
        \t\t\t\t\t\t\t\t\t                ╚══════╝                   ╚══════╝                 ╚═════╝ 
        \t\t\t\t\t\t\t\t\t
        \t\t\t\t\t\t\t\t\t            ██╗                      ██╗                      ██╗                      ██╗
        \t\t\t\t\t\t\t\t\t          ██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗
        \t\t\t\t\t\t\t\t\t          ╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝
        \t\t\t\t\t\t\t\t\t            ╚═╝                      ╚═╝                      ╚═╝                      ╚═╝
        \t\t\t\t\t\t\t\t\t
        \t\t\t\t\t\t\t\t\t  ███╗      ██╗ """,form11,"""     ██╗ """,form21,"""     ██╗ """,form31,"""     ██╗  
        \t\t\t\t\t\t\t\t\t ████║      ██║ """,form12,"""     ██║ """,form22,"""     ██║ """,form32,"""     ██║ 
        \t\t\t\t\t\t\t\t\t██╔██║      ██║ """,form13,"""     ██║ """,form23,"""     ██║ """,form33,"""     ██║  
        \t\t\t\t\t\t\t\t\t╚═╝██║      ██║ """,form14,"""     ██║ """,form24,"""     ██║ """,form34,"""     ██║  
        \t\t\t\t\t\t\t\t\t███████╗    ██║ """,form15,"""     ██║ """,form25,"""     ██║ """,form35,"""     ██║  
        \t\t\t\t\t\t\t\t\t╚══════╝    ╚═╝ """,form16,"""     ╚═╝ """,form26,"""     ╚═╝ """,form36,"""     ╚═╝  
        \t\t\t\t\t\t\t\t\t            ██╗                      ██╗                      ██╗                      ██╗
        \t\t\t\t\t\t\t\t\t          ██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗
        \t\t\t\t\t\t\t\t\t          ╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝
        \t\t\t\t\t\t\t\t\t            ╚═╝                      ╚═╝                      ╚═╝                      ╚═╝
        \t\t\t\t\t\t\t\t\t
        \t\t\t\t\t\t\t\t\t██████╗     ██╗ """,form41,"""     ██╗ """,form51,"""     ██╗ """,form61,"""     ██╗  
        \t\t\t\t\t\t\t\t\t╚════██╗    ██║ """,form42,"""     ██║ """,form52,"""     ██║ """,form62,"""     ██║ 
        \t\t\t\t\t\t\t\t\t  ███╔═╝    ██║ """,form43,"""     ██║ """,form53,"""     ██║ """,form63,"""     ██║  
        \t\t\t\t\t\t\t\t\t██╔══╝      ██║ """,form44,"""     ██║ """,form54,"""     ██║ """,form64,"""     ██║  
        \t\t\t\t\t\t\t\t\t███████╗    ██║ """,form45,"""     ██║ """,form55,"""     ██║ """,form65,"""     ██║  
        \t\t\t\t\t\t\t\t\t╚══════╝    ╚═╝ """,form46,"""     ╚═╝ """,form56,"""     ╚═╝ """,form66,"""     ╚═╝ 
        \t\t\t\t\t\t\t\t\t            ██╗                      ██╗                      ██╗                      ██╗
        \t\t\t\t\t\t\t\t\t          ██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗
        \t\t\t\t\t\t\t\t\t          ╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝
        \t\t\t\t\t\t\t\t\t            ╚═╝                      ╚═╝                      ╚═╝                      ╚═╝
        \t\t\t\t\t\t\t\t\t
        \t\t\t\t\t\t\t\t\t██████╗     ██╗ """,form71,"""     ██╗ """,form81,"""     ██╗ """,form91,"""     ██╗  
        \t\t\t\t\t\t\t\t\t╚════██╗    ██║ """,form72,"""     ██║ """,form82,"""     ██║ """,form92,"""     ██║ 
        \t\t\t\t\t\t\t\t\t █████╔╝    ██║ """,form73,"""     ██║ """,form83,"""     ██║ """,form93,"""     ██║  
        \t\t\t\t\t\t\t\t\t ╚═══██╗    ██║ """,form74,"""     ██║ """,form84,"""     ██║ """,form94,"""     ██║  
        \t\t\t\t\t\t\t\t\t██████╔╝    ██║ """,form75,"""     ██║ """,form85,"""     ██║ """,form95,"""     ██║  
        \t\t\t\t\t\t\t\t\t╚═════╝     ╚═╝ """,form76,"""     ╚═╝ """,form86,"""     ╚═╝ """,form96,"""     ╚═╝ 
        \t\t\t\t\t\t\t\t\t            ██╗                      ██╗                      ██╗                      ██╗
        \t\t\t\t\t\t\t\t\t          ██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗█████╗█████╗█████╗██████╗
        \t\t\t\t\t\t\t\t\t          ╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝╚════╝╚════╝╚════╝╚═██╔═╝
        \t\t\t\t\t\t\t\t\t            ╚═╝                      ╚═╝                      ╚═╝                      ╚═╝""")

if round==0:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
    print("\t\t\t\t\t\t\t\t\t\t ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
    print("\t\t\t\t\t\t\t\t\t\t ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
    print("\t\t\t\t\t\t\t\t\t\t ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
    print("\t\t\t\t\t\t\t\t\t\t ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
    print("\t\t\t\t\t\t\t\t\t\t ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
    print("\n\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ████████╗░█████╗░")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ╚══██╔══╝██╔══██╗")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░██║░░██║")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░██║░░██║")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░╚█████╔╝")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░╚═╝░░░░╚════╝░")
    print("\n\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t████████╗██╗░█████╗░████████╗░█████╗░░█████╗░████████╗░█████╗░███████╗")
    print("\t\t\t\t\t\t\t\t\t\t╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝")
    print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║██║░░╚═╝░░░██║░░░███████║██║░░╚═╝░░░██║░░░██║░░██║█████╗░░")
    print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║██║░░██╗░░░██║░░░██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══╝░░")
    print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║╚█████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝███████╗")
    print("\t\t\t\t\t\t\t\t\t\t░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚══════╝")
    print("")
    if text==4:
        print("\n")
        print("\t\t\t\t\t\t\t\t\t█▀▀▄ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀█ ░▀░ █▀▀ █▀▀▄ 　 ▒█░░░ █░░█ █▀▀ █▀▀█ █░░█ ░▀░ █▀▀█ █░░█ █▀▀▄ ")
        print("\t\t\t\t\t\t\t\t\t█▀▀▄ █▄▄█ 　 ▒█▄▄█ █░░█ █▄▄▀ ▀█▀ █▀▀ █░░█ 　 ▒█░░░ █░░█ █░░ █░░█ █░░█ ▀█▀ █▄▄█ █░░█ █░░█ ")
        print("\t\t\t\t\t\t\t\t\t▀▀▀░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░░▀ 　 ▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀█ ░▀▀▀ ▀▀▀ ▀░░▀ ░▀▀▀ ▀▀▀░")
        print("\n\n\n\n")
        print("")
    elif text==3:
            print("\n\n\t\t\t\t\t\t\t\t  _                         _      _              _                           _                 _ ")
            print("\t\t\t\t\t\t\t\t | |               /\      | |    (_)            | |                         (_)               | |")
            print("\t\t\t\t\t\t\t\t | |__  _   _     /  \   __| |_ __ _  ___ _ __   | |    _   _  ___ __ _ _   _ _  __ _ _   _  __| |")
            print("\t\t\t\t\t\t\t\t | '_ \| | | |   / /\ \ / _` | '__| |/ _ \ '_ \  | |   | | | |/ __/ _` | | | | |/ _` | | | |/ _` |")
            print("\t\t\t\t\t\t\t\t | |_) | |_| |  / ____ \ (_| | |  | |  __/ | | | | |___| |_| | (_| (_| | |_| | | (_| | |_| | (_| |")
            print("\t\t\t\t\t\t\t\t |_.__/ \__, | /_/    \_\__,_|_|  |_|\___|_| |_| |______\__,_|\___\__, |\__,_|_|\__,_|\__,_|\__,_|")
            print("\t\t\t\t\t\t\t\t         __/ |                                                       | |       ")
            print("\t\t\t\t\t\t\t\t        |___/                                                        |_|    ")
            print("")
            print("\n\n\n\n")
    elif text==2:
        print("\n\n\t\t\t\t\t\t\t     ████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("\t\t\t\t\t\t\t     █▄─▄─▀█▄─█─▄████▀▄─██▄─▄▄▀█▄─▄▄▀█▄─▄█▄─▄▄─█▄─▀█▄─▄███▄─▄███▄─██─▄█─▄▄▄─█─▄▄▄─█▄─██─▄█▄─▄██▀▄─██▄─██─▄█▄─▄▄▀█")
        print("\t\t\t\t\t\t\t     ██─▄─▀██▄─▄█████─▀─███─██─██─▄─▄██─███─▄█▀██─█▄▀─█████─██▀██─██─██─███▀█─██▀─██─██─███─███─▀─███─██─███─██─█")
        print("\t\t\t\t\t\t\t     ▀▄▄▄▄▀▀▀▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀")
        print("\n\n\n\n\n")
    elif text==6:
            print("\t\t\t\t\t\t\t\t\t\t█▄▄ █▄█   ▄▀█ █▀▄ █▀█ █ █▀▀ █▄░█   █░░ █░█ █▀▀ █▀█ █░█ █ ▄▀█ █░█ █▀▄")
            print("\t\t\t\t\t\t\t\t\t\t█▄█ ░█░   █▀█ █▄▀ █▀▄ █ ██▄ █░▀█   █▄▄ █▄█ █▄▄ ▀▀█ █▄█ █ █▀█ █▄█ █▄▀")
            print("\n\n\n\n\n\n\n\n\n\n")
    elif text==1:
            print("")
            print("\t\t\t\t\t\t\t\t\t       _          _____   _     _            __                    _           _ ")
            print("\t\t\t\t\t\t\t\t\t      | |_ _ _   |  _  |_| |___|_|___ ___   |  |   _ _ ___ ___ _ _|_|___ _ _ _| |")
            print("\t\t\t\t\t\t\t\t\t      | . | | |  |     | . |  _| | -_|   |  |  |__| | |  _| . | | | | .'| | | . |")
            print("\t\t\t\t\t\t\t\t\t      |___|_  |  |__|__|___|_| |_|___|_|_|  |_____|___|___|_  |___|_|__,|___|___|")
            print("\t\t\t\t\t\t\t\t\t          |___|                                             |_| ")
            print("\n\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t    Press 's' to start\n\n\n")
    start=input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t     ")           

if start==("s"):
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t     Started the game\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#ist entfernbar / nicht benötigt
    while fofo==1:
        if form=="O":
            form_x1=("      ██╗  ██╗")
            form_x2=("      ╚██╗██╔╝")
            form_x3=("       ╚███╔╝ ")
            form_x4=("       ██╔██╗ ")
            form_x5=("      ██╔╝╚██╗")
            form_x6=("      ╚═╝  ╚═╝")
        elif form=="X":
            form_x1=("       █████╗ ")
            form_x2=("      ██╔══██╗")
            form_x3=("      ██║  ██║")
            form_x4=("      ██║  ██║")
            form_x5=("      ╚█████╔╝")
            form_x6=("       ╚════╝")
        print_table(0)
        change_player(0)
        print ("\n\t\t\t\t\t\t\t\t\t\t\t\t\tSpieler",player,"(",form,")"" ist dran.")
        x= int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\tPosition x:"))
        y= int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\tPosition y:"))
        print("\n\n\n\n\n")  
        
        if x==1 and y==2 and form41=="              ":
            form41=form_x1
            form42=form_x2
            form43=form_x3
            form44=form_x4
            form45=form_x5
            form46=form_x6
        elif x==1 and y==1 and form11=="              ":
            form11=form_x1
            form12=form_x2
            form13=form_x3
            form14=form_x4
            form15=form_x5
            form16=form_x6
        elif x==1 and y==3 and form71=="              ":
            form71=form_x1
            form72=form_x2
            form73=form_x3
            form74=form_x4
            form75=form_x5
            form76=form_x6
        elif x==2 and y==1 and form21=="              ":
            form21=form_x1
            form22=form_x2
            form23=form_x3
            form24=form_x4
            form25=form_x5
            form26=form_x6
        elif x==2 and y==3 and form81=="              ":
            form81=form_x1
            form82=form_x2
            form83=form_x3
            form84=form_x4
            form85=form_x5
            form86=form_x6
        elif x==2 and y==2 and form51=="              ":
            form51=form_x1
            form52=form_x2
            form53=form_x3
            form54=form_x4
            form55=form_x5
            form56=form_x6
        elif x==3 and y==3 and form91=="              ":
            form91=form_x1
            form92=form_x2
            form93=form_x3
            form94=form_x4
            form95=form_x5
            form96=form_x6
        elif x==3 and y==2 and form61=="              ":
            form61=form_x1
            form62=form_x2
            form63=form_x3
            form64=form_x4
            form65=form_x5
            form66=form_x6
        elif x==3 and y==1 and form31=="              ":
            form31=form_x1
            form32=form_x2
            form33=form_x3
            form34=form_x4
            form35=form_x5
            form36=form_x6
        elif x>3 or y>3:
            print(bcolors.WARNING +"\n\n\t\t\t\t\t\t\t\t\t\t\t\tError - Falsche Eigabe! (Wähle zwischen 1-3)!\n\n"+bcolors.ENDC)
            change_player(0)
        else:
            print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t"+bcolors.WARNING + "Unmöglicher Spielzug! Feld bereits besetzt!\n\n"+bcolors.ENDC)
            change_player(0)
        if form11==form21==form31==("      ██╗  ██╗") or form41==form51==form61==("      ██╗  ██╗") or form71==form81==form91==("      ██╗  ██╗") or form11==form41==form71==("      ██╗  ██╗") or form21==form51==form81==("      ██╗  ██╗") or form31==form61==form91==("      ██╗  ██╗") or form11==form51==form91==("      ██╗  ██╗") or form71==form51==form31==("      ██╗  ██╗") or form11==form21==form31==("       █████╗ ") or form41==form51==form61==("       █████╗ ") or form71==form81==form91==("       █████╗ ") or form11==form41==form71==("       █████╗ ") or form21==form51==form81==("       █████╗ ") or form31==form61==form91==("       █████╗ ") or form11==form51==form91==("       █████╗ ") or form71==form51==form31==("       █████╗ "):
            print_table(0)
            if form=="X":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t     "+bcolors.WARNING+"Player 1 (X) won!\n"+bcolors.ENDC)
                aktion_passiert=1
            elif form=="O":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t     "+bcolors.WARNING+"Player 2 (O) won!\n"+bcolors.ENDC)
                aktion_passiert=1
            

        if form11!=("              ") and form21!=("              ") and form31!=("              ") and form41!=("              ") and form51!=("              ") and form61!=("              ") and form71!=("              ") and form81!=("              ") and form91!=("              ") and aktion_passiert==0:
            print_table(0)
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t  "+bcolors.WARNING +"Game is over! Nobody won!\n\n"+bcolors.ENDC)
            aktion_passiert=1
        
    
        if aktion_passiert==1:
            opa=input("\t\t\t\t\t\t\t\t\t\t\t\t     "+bcolors.WARNING+"Type 'r' to restart or 'e' to end: "+bcolors.ENDC)
            print("\n\n\n\n")
            popo=1
            if opa=="r":
                fofo=1
                form11=form12=form13=form14=form15=form16=form21=form22=form23=form24=form25=form26=form31=form32=form33=form34=form35=form36=form41=form42=form43=form44=form45=form46=form51=form52=form53=form54=form55=form56=form61=form62=form63=form64=form65=form66=form71=form72=form73=form74=form75=form76=form81=form82=form83=form84=form85=form86=form91=form92=form93=form94=form95=form96=("              ")
                aktion_passiert=0
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\t\t\t\t\t\t\t\t\t\t ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗  ███████╗░█████╗░██████╗░")
                print("\t\t\t\t\t\t\t\t\t\t ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗")
                print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░  █████╗░░██║░░██║██████╔╝")
                print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗")
                print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝  ██║░░░░░╚█████╔╝██║░░██║")
                print("\t\t\t\t\t\t\t\t\t\t ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝\n")
                print("\t\t\t\t\t\t\t\t\t\t\t    ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░")
                print("\t\t\t\t\t\t\t\t\t\t\t    ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░")
                print("\t\t\t\t\t\t\t\t\t\t\t    ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░")
                print("\t\t\t\t\t\t\t\t\t\t\t    ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗")
                print("\t\t\t\t\t\t\t\t\t\t\t    ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝")
                print("\t\t\t\t\t\t\t\t\t\t\t    ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                fofo=0
