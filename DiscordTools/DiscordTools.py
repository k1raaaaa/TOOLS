#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
os.system("title TOOLS CREATE BY ZERFOX ")
import colorama
from colorama import Fore
from colorama import Style
from colorama.initialise import reset_all


colorama.init()

def intro():
    
    print(Fore.BLUE + """
████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                           """ + Style.RESET_ALL)
    print(Fore.MAGENTA +"\n\nCreate by Zerfox | My github is https://github.com/pommepoirechocolat  | BETA\n\n" + Style.RESET_ALL)
    x = input("[1] Discord  [2]autre \n\n choisie un nombres:  ")

    if x == '1':
        main()

    if x == '2':
        autre()








def main():
    
    print(Fore.RED +"""

████████╗ ██████╗  ██████╗ ██╗     ███████╗      ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝      ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║██║   ██║██║     ███████╗█████╗██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
   ██║   ██║   ██║██║   ██║██║     ╚════██║╚════╝██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║      ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                                         BETA

""" + Style.RESET_ALL)

    n = input("""  [1]Gen        [2]Webhook        [3]token     [4]Raid  [m]menu\n\nChoisie un nombre:  """)
    if n == '1':
        Generateur()

    if n == '2':
        weebhook()

    if n == '3':
        bot()

    if n == '4':
        Raid()

    if n == 'm':
        intro()


def Generateur():
    
    print(Fore.MAGENTA + """



 ██████╗ ███████╗███╗   ██╗
██╔════╝ ██╔════╝████╗  ██║
██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                      

    """ + Style.RESET_ALL)
    f = input("[1]Nitro  [2]Proxie  [m]menu \nChoisie un nombre ")

    if f == '1':
        Nitro()

    if f == 'm':
        main()

    if f == '2':
        proxiegen()





def Nitro():
    
    print(Fore.YELLOW +""" 

███╗   ██╗██╗████████╗██████╗  ██████╗        ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗      ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝      ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                                                                          
             
             
             """ + Style.RESET_ALL)  
    
    v = input("[1] Gen + Checker [m] menu\n\nChoisie 1 pour générer des code nitro:  ")

    if v == '1':
        Gen()

    if v == 'm':
        Generateur()

def Gen():
    
    print(Fore.MAGENTA + """
███╗   ██╗██╗████████╗██████╗  ██████╗        ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗      ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝      ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                        
    """ + Style.RESET_ALL)
    import random, string
    import webbrowser
    import time
    import requests
    num=input('\nCombien de Code: ')
    f=open("Nitro Codes.txt","w", encoding='utf-8')
    print("\nGénération des code en cour...")
    
    for n in range(int(num)):
        y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        
        f.write('https://discord.gift/')
        f.write(y)
        f.write("\n")
    f.close()  
    with open("Nitro Codes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            
            if r.status_code == 200:
                print(Fore.GREEN + " Valide | {} ".format(line.strip("\n" + Style.RESET_ALL)))
                break
            else:
                print(Fore.RED + " Invalide | {} ".format(line.strip("\n" + Style.RESET_ALL)))




def proxiegen():
    
    print(Fore.RED + """

██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                  
""" + Style.RESET_ALL)

    w = input ("[1]Gen   [m] Menu \n\n Choisie un nombre:  ")

    if w == '1':    
        popop()

    if w == 'm':
        main()
    


def popop():
    
    print(Fore.GREEN + """
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗       ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝      ██╔════╝ ██╔════╝████╗  ██║
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████║      ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                   
    """ + Style.RESET_ALL)
    from bs4 import BeautifulSoup as bs
    import random as rn
    import os
    import requests as rq

    print("Vos proxie vont apparaitre dans quelque seconde!")

    n = "\033[m"
    r = "\033[1;31m"
    g = "\033[1;32m"
    y = "\033[1;33m"
    w = "\033[1;37m"
    b = "\033[1;34m"
    p = "\033[1;35m"
    cy = "\033[1;36m"

    colors = [r,g,y,w,b,p,cy]

    headers = {'User-Agent' : 'Mozilla/5.0'}

    r = rq.get("https://www.us-proxy.org/",headers=headers).text

    s = bs(r,"html.parser")
    hosts = s.find("textarea",{"class":"form-control"})

    list = (hosts.text).split("\n")
    for host in list:
        color = rn.choice(colors)
        if host == "":
            continue
        else:
            print(color+host+n)














def weebhook():
    
    print(Fore.MAGENTA + """

██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗███████╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ ███████╗
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ ╚════██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗███████║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                    
         
         """ + Style.RESET_ALL)
    
    l = input("\n[1]spam    [2]suprimé  [3]evoyer un message  [m]menu \nchoisir un nombre:  ")

    if l == '1':
        Spam()

    if l == '2':
        deleted()


    if l == '3':
        message()

    if l == 'm':
        main()


def Spam():
    
    print(Fore.RED + """
███████╗██████╗  █████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║
███████╗██████╔╝███████║██╔████╔██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
███████║██║     ██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                   
    """ + Style.RESET_ALL)
    import discord_webhook
    from discord_webhook import DiscordEmbed, DiscordWebhook
    import string
    import time
    import requests
    import colorama
    import json
    from colorama import Fore

    colorama.init()

    def webhkspammer():
        webhook = input("\n[>] url du webhook:  ")
        message = input("\n[>] Que veux tu spam:  ")
        delay = float(input("\n[>] l'interval entre chaque message (exemple: 0.5):  "))

        while True:
            print(Fore.BLUE + "Envoie ---> " + message)
            print(Fore.RESET + " ")
            try:
                time.sleep(delay)
                _data = requests.post(webhook, json={'content': message})

                if _data.status_code == 204:
                    print(Fore.YELLOW + "envoyé --> " + message)
            except:
                print("Quelque chose est arrivé ! Webhook probablement cassé" + weebhook)
                time.sleep(5)
                exit()
    x = 5
    while x == 5:
        webhkspammer()

def deleted():
    
    print(Fore.YELLOW + """
██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██║  ██║
██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██║  ██║
██████╔╝███████╗███████╗███████╗   ██║   ███████╗██████╔╝
╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═════╝ 
                                                         """ + Style.RESET_ALL)
    import colorama
    import requests
    import ctypes
    import datetime
    import os
    import time
    from datetime import date
    from colorama import Fore, Back, Style

    colorama.init()

    count = 0
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    ctypes.windll.kernel32.SetConsoleTitleW(f'Webhook Deleter | {d2}')

    p = f'{Style.BRIGHT + Fore.MAGENTA}'
    w = f'{Style.BRIGHT + Fore.WHITE}'

    webhook = input("Webhook url : ")
    requests.delete(webhook).text   
    print(f"\n{w}le {p}Webhook {w}à bien etai suprimé{p}\n")
    time.sleep(1.5)



def message():
    
    print(Fore.MAGENTA + """

███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗
████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝
██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  
██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  
██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                            
    """ + Style.RESET_ALL)
    from discord_webhook import DiscordWebhook
    url = input("[>] url du webhook:  ")
    message = input("\n [>] quel est le message a envoyer:  ")
    webhook_url = [url]
    webhook = DiscordWebhook(url=webhook_url, content= message)
    response = webhook.execute()
    print(Fore.RED + "\n [...]message ben envoyer" + Style.RESET_ALL)





def bot():          
   
    print(Fore.YELLOW + """

████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ (la catégorie token sera mener a evoluer)
                                                                                
                                                                                                                                                                                                                                                                                                        
    """ + Style.RESET_ALL)

    p = input ("[1]Token Check     [m] Menu\nVeuiller entré un nombre: ")

    if p == '1':
        checkeur()


    if p == 'm':
        main()



def checkeur():
    
    print(Fore.GREEN + """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗       ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║█████╗██║     ███████║█████╗  ██║     █████╔╝ 
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                                          
    """ + Style.RESET_ALL)
    import requests
    print(Fore.RED + "Merci de metre dans le fichier un fichier texte nommé tokens.txt " + Style.RESET_ALL)
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip("\n")
            headers = {'Content-Type': 'application/json', 'authorization': token}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print("{} Fonctionel :)".format(line.strip("\n")))
            else:
                print("Token non fonctionel")
    y = input (Fore.RED + "Pour revenir au menu metez un m:  " + Style.RESET_ALL)

    if y == 'm':
        main()







def Raid():
    
    print(Fore.RED + """

██████╗  █████╗ ██╗██████╗ 
██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝███████║██║██║  ██║
██╔══██╗██╔══██║██║██║  ██║
██║  ██║██║  ██║██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ 
                           
 """ + Style.RESET_ALL)
    h = input ("[1] RAID BOT   [m] menu \n choisie un nombre:  ")

    if h == '1':
        RaidBot()

    if h == 'm':
        main()



def RaidBot():
    
    print(Fore.BLUE + """
██████╗  █████╗ ██╗██████╗       ██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██║██╔══██╗      ██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║██║  ██║█████╗██████╔╝██║   ██║   ██║   
██╔══██╗██╔══██║██║██║  ██║╚════╝██╔══██╗██║   ██║   ██║   
██║  ██║██║  ██║██║██████╔╝      ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝       ╚═════╝  ╚═════╝    ╚═╝   
                                                           
    """ + Style.RESET_ALL)
    import discord,os,asyncio
    from discord.ext import commands, tasks
    
    tokenraid = input ("\n\nToken du Bot:")
    prefix = input ("choisi le péfix:  ")
    nameserveur = input ("Quel nom pour le serveur:  ")
    channelname = input ("Nom des channel créé:  ")
    messagesend = input ("message a spam:  ")
    messagesend2 = input ("autre message a spam:  ")
    print ("Le Raid va commencer !")
    print ("la commande pour lancer le spam est:" + prefix + "spam")
    prefix= prefix
    
    client = commands.Bot(command_prefix=prefix)

    @client.event
    async def on_ready():
        print(Fore.GREEN + "Bot opérationelle ")
        await client.change_presence(activity=discord.Game(name="Bot create by Zerfox | my github: https://github.com/pommepoirechocolat"))

    with open ('logo.png','rb') as f:
        icon = f.read()

    @client.command()
    async def  spam(ctx):
        
        await ctx.guild.edit(name=nameserveur, icon=icon) 
        guild = ctx.message.guild 
            
        n = 0
        while(n<=500):
            await guild.create_text_channel(channelname)
            await ctx.channel.send(messagesend)
            await ctx.channel.send(messagesend2)
            n = n + 1
    
    TOKEN = tokenraid
    client.run(TOKEN)




def autre():
    
    print(Fore.RED + """
 
 █████╗ ██╗   ██╗████████╗██████╗ ███████╗
██╔══██╗██║   ██║╚══██╔══╝██╔══██╗██╔════╝
███████║██║   ██║   ██║   ██████╔╝█████╗  
██╔══██║██║   ██║   ██║   ██╔══██╗██╔══╝  
██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝

    """ + Style.RESET_ALL)
    
    gh = input("[1]Download   [2]Location  [3]spammer [m]menu  ")

    if gh == '1':
        téléchargement()

    if gh == 'm':
        main()

    if gh == '2':
        jeu()

    if gh == '3':
        spammed()






def téléchargement():
    
    print(Fore.YELLOW + """

██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                      
                                                                                                                          
    """ + Style.RESET_ALL)
    p = input("[1]youtube  [m]menu \n\n choisie un nombre:  ")

    if p == 'm':
        intro()

    if p == '1':
        youtube()







def youtube():
    
    print(Fore.RED + """
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                                             
    """ + Style.RESET_ALL)
    from pytube import YouTube
    import time
    url = input("URL de la video:   ")
    time.sleep(1)
    print("#.........10%")
    video = YouTube(url)
    print("##........20%")
    print("titre: " + video.title)
    print("###.......30%")
    time.sleep(2)
    print("#####.....50%")
    video = video.streams.get_highest_resolution()
    print("#########.90%")
    time.sleep(1)
    print("##########100%")
    video.download()
    print("video bien télécharger :)")






def jeu():
    
    print(Fore.GREEN + """

██╗      ██████╗  ██████╗ █████╗ ████████╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ███████║   ██║   █████╗  ██║  ██║
██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  ██║  ██║
███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ███████╗██████╔╝
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 
    """ + Style.RESET_ALL)

    t = input("[1 ]ip [m]menu  \nchoisie un nombre:")

    if t == '1':
        ip()


    if t == 'm':
        main()


def ip():
    
    print(Fore.YELLOW + """
██╗██████╗       ██╗      ██████╗  ██████╗ █████╗ ████████╗███████╗██████╗ 
██║██╔══██╗      ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║██████╔╝█████╗██║     ██║   ██║██║     ███████║   ██║   █████╗  ██║  ██║
██║██╔═══╝ ╚════╝██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  ██║  ██║
██║██║           ███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ███████╗██████╔╝
╚═╝╚═╝           ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 
                                                                           
    """ + Style.RESET_ALL)

    import requests
    import json
    import os

    ip = input("entre l'adresse ip:  "); ip.replace(" ", "")

    r = requests.get(f"http://ip-api.com/json/{ip}")
    r2 = requests.get(f"https://ipinfo.io/{ip}")
    values = json.loads(r.text)
    data = r2.json()
    city = data["city"]
    location = data["loc"].split(",")
    latitude = location[0]
    longitude = location[1]

    print("\n [1] : " + values["country"] + f" [{values['countryCode']}]")
    print(" [2] : " + values["regionName"] + f" [{values['region']}]")
    print(" [3] : " + city)
    print(" [4] : " + values["timezone"])
    print(" [5] : " + values["isp"])
    print(" [6] : " + latitude, "|", longitude)


def spammed():
  
    print(Fore.BLUE + """
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)

    a = input("[1]mail  [m]menu \nchoisie un nombre:  ")

    if a == '1':
        mail()

    if a == 'm':
        main()


def mail():
    import smtplib
    from email.message import EmailMessage
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    victime = input("mail de la victime:  ")
    you = input("ton email:  ")
    password = input("ton mot de passe:  ")
    sujet = input("sujet de ton message:  ")
    sendg = input("message a envoiyer:  ")

    
    spam_count = 10             
    email_addr = victime   
    to_email = you    
    password = password           
    subject = sujet  
    
    msg = EmailMessage()
    
    msg['Subject'] = subject
    msg['From'] = email_addr
    msg['To'] = to_email
    msg.set_content(sendg)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_addr, password)
        for i in range(spam_count):
            smtp.send_message(msg)






if __name__ == "__main__":
    intro()