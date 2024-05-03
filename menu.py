def menu(invoer=0):
    if invoer!=0:
        from check import serverToevoegen, serverTonen, serverPing
        match invoer:
            case 1:
                serverToevoegen()
            case 2:
                serverTonen()
            case 3:
                serverPing()
    else:
        print("\nhallo, welkom bij server checker, welke actie zou je willen doen?")
        print("1. server toevoegen")
        print("2. servers tonen (lijst)")
        print("3. pingen naar servers")
        print("0. om te stoppen")
        try:
            invoer=int(input("[1/2/3/0   def:2]: "))
            if(invoer == 0):
                print("programma over :(")
                quit()
            elif invoer in [1,2,3]:
                from check import serverToevoegen, serverTonen, serverPing
                match invoer:
                    case 1:
                        serverToevoegen()
                    case 2:
                        serverTonen()
                    case 3:
                        serverPing()
            else:
                print("invoer ongeldig! einde programma!")
                quit()
        except ValueError:
            from check import serverTonen
            serverTonen()