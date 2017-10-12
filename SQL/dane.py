#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import csv

def dane_z_pliku(plik):
    dane = []
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delmiter='\t')
        for rekort in tresc:
            dane.append(rekord)
    return dane


def main(args):
    
    premia = dane_z_pliku('premia.txt')
    print(premia)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
