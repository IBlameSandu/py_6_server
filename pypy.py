from ping3 import ping

def pinging(host):
    response = ping(host)
    return True if response else False #als 0 dan true anders false

print(pinging("google.com"))