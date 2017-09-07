#!/usr/bin/env python
# -*- coding: utf-8 -*-

ROK_TERAZ = 2017
ROK_PY = 1991

def parzyste(n):
    ile = list(range(0, n+1, 2))
    print(ile)
    return len(ile)

def main(args):
    imie = input("Imię? ")
    wiek = int(input("ile masz lat? "))
    rok_urodzenia = ROK_TERAZ - wiek
    print ("witaj", imie)
    print ("Urodziłeś się w: ", ROK_TERAZ-wiek)
    
    if ROK_PY < rok_urodzenia:
        print("Jestem starszy")
    elif ROK_PY > rok_urodzenia:
        print("jestem młodszy")
    elif ROK_PY == rok_urodzenia:
        print("tyle samo lat")
    
    n = int(input("Podaj liczbę naturalną: "))
    print("Ilość parzystych: ", parzyste(n))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
