import sys
from menu import menu

def main():
    keuzen=[1,2,3,0]
    if len(sys.argv) > 1:
        if int(sys.argv[1]) in keuzen:
            menu(int(sys.argv[1]))
    else:
        while True:
            menu()

if __name__=="__main__":
    main()