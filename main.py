# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Beispiele
# print_hi('PyCharm')
#                  0      1       2
# begruessen = ['hello', 'hi', 'hallo']
# begruessen.append('hey')    # hey wird an das Ende von begruessen angehangt
# begruessen.insert(0, 'hey')    # hey wird an den start von begruessen angehängt
# begruessen.sort()    # sortiert begruessen alphabetisch
# print_list(begruessen)
# input1 = input() # Eingabe mit input()
# print(input1)    # Ausgabe mit print()


# Stuckturvorlage main
# Listen/Dictionaries? werden mit Dateiinhalten gefüllt
# Schleife
# Programm bekommt Eingabe
# Eingabe wird auf Abbruchbedingung geprüft
# Programm ruft Funktion zur findung einer Antwort auf
# Listen/Dictionaries? werden in Dateien gespeichert

# Strukturvorlage antwort_finden
# eingabe wird analysiert
# if eingabe ist in liste von Antwortkategorien
# passende Antwortfunktion wird aufgerufen
# else
# zufällige entschuldigung

#

import pickle as p  # wird eventuell wieder entfernt
from random import randrange

# Variablen die in mehreren Bereichen genutzt werden
begruessung = ['Hallo', 'Hey', 'Guten Tag', 'Hi', 'Moin']
verabschiedung = ['Tschüss', 'Bye', 'Auf Wiedersehen']


def wegschreiben(liste, dateiname):    # todo auf JSON ansehen
    with open(dateiname, 'wb') as tmp:
        p.dump(liste, tmp)



# def einlesen(dateiname, liste):
# with open(dateiname, 'rb') as tmp:
# liste = p.load(tmp)


def antwort_finden(eingabe):  # Groß- und Kleinschreibung sollte bei "eingabe" uninteressant sein

    if eingabe.lower() in (begr.lower() for begr in begruessung):
        return begruessung[randrange(len(begruessung))]  # Zufällige Antwort aus bergruessung
    else:
        if eingabe in (verab.lower() for verab in verabschiedung):
            return verabschiedung[randrange(len(verabschiedung))]  # Zufällige Antwort aus verabschiedung
        else:
            return "Ich habe Sie nicht verstanden."  # todo Eweiterung mit Liste von Entschuldigungen


def simple_chat_bot():
    eingabe = ""  # ist lokale Variable?
    while eingabe not in (verab.lower() for verab in verabschiedung):
        eingabe = input()
        antwort = antwort_finden(eingabe)
        print(antwort)
    wegschreiben(verabschiedung, 'verabschiedung.txt')


if __name__ == '__main__':
    simple_chat_bot()
