import json
import socket
from ping3 import ping
from datetime import datetime
from menu import menu

def serverToevoegen():
    '''server toevoegen aan de json bestand waar de servers in opgeslagen worden'''

    toevoegen = False
    struc = ""

    invoer = input("Welke server wil je toevoegen? \n")
    try:
        with open("servers.json", "r") as bestand:
            servers = json.load(bestand)
            server_names = [item["naam"] for item in servers]
            struc = invoer
            if struc in server_names:
                print("Server is al toegevoegd")
            else:
                toevoegen = True
                print("Nieuwe server, ik zal het toevoegen!")
    except json.decoder.JSONDecodeError:
        servers=[]
        struc=invoer
        toevoegen = True
        print("Nieuwe server, ik zal het toevoegen!")
    
    if toevoegen:
        servers.append({"naam": struc})
        with open("servers.json", "w") as bestand:
            json.dump(servers, bestand, indent=2)

    menu()

def pinging(host):
    #response = ping(host)
    #return True if response else False #als 0 dan true anders false
    return True

def html():
    with open("index.html","w") as index:
        index.write(f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8' /><meta name='viewport' content='width=device-width, initial-scale=1.0' /><link rel='stylesheet' href='style.css' /><title>server statuses</title></head><body><h2>Labo 6 python, Server ok?</h2>")
        with open("data.json","r") as bestand:
            data=json.load(bestand)
            for x in data:
                ip=socket.gethostbyname(x["naam"])
                index.write(f"<div><h1>{str(x['naam'])}</h1><h1>{str(ip)}</h1><h1>{str(pinging(ip))}</h1></div>")
        index.write("</body></html>")    

def serverTonen():
    html()
    with open("servers.json", "r") as bestand:
        servers=json.load(bestand)
    print("\n")
    print(f"nummer".center(35) + "|" + "naam".center(35) + "|" + "ip".center(35) + "|" + "ok?".center(35))
    for x in range(0, len(servers)):
        ip=socket.gethostbyname(servers[x]["naam"])
        print(str(x+1).center(35) + "|" + str(servers[x]["naam"]).center(35) + "|" + str(ip).center(35) + "|" + str(pinging(ip)).center(35))
    print('\n\n')
    menu()

def serverPing():
    try:
        with open("data.json", "r") as bestand:
            old_records=json.load(bestand)
    except json.decoder.JSONDecodeError:
        old_records=[]
    
    with open("servers.json", "r") as bestand:
        servers=json.load(bestand)
    
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S %d/%m/%Y")

    new_records=[]
    
    for server in servers:
        ping = pinging(server["naam"])
        ping_struc={"naam":server["naam"],"time":dt_string,"ping":ping}
        new_records.append(ping_struc)

    all_rec=new_records+old_records
    with open("data.json", "w") as bestand:
        json.dump(all_rec, bestand)
    
    print("alle pings werden gedaan!")

    serverTonen()