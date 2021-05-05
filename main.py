
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

# Struckturvorlage antwort_finden
# eingabe wird analysiert
# if eingabe ist in liste von Antwortkategorien
    # passende Antwortfunktion wird aufgerufen
# else
    # zufällige entschuldigung
    # fragen ob die frage zu einer der Vorhandenen Antwortkategorieren passt
    # if ja
        # zu passender Liste/Dictionary? hinzufügen
    # else
        # fragen ob neue Antwortkategorie erstellt werden soll
        # if ja
            # erstellen
            # nach passenden Antworten fragen
        #else
            #return?

#

import pickle    # wird eventuell wieder entfernt
from random import randrange

# Variablen die in mehreren Bereichen genutzt werden
begruessung = ['Hallo', 'Hey', 'Guten Tag', 'Hi', 'Moin']
verabschiedung = ['Tschüss', 'Bye', 'Auf Wiedersehen']


def wegschreiben(liste, dateiname):
    with open(dateiname, 'wb') as tmp:
        pickle.dump(liste, tmp)


# def einlesen(dateiname, liste):
    # with open(dateiname, 'rb') as tmp:
        # liste = pickle.load(tmp)


def antwort_finden(eingabe):    # todo Groß- und Kleinschreibung sollte bei "eingabe" uninteressant sein

    if eingabe in begruessung:
        return begruessung[randrange(len(begruessung))]   # Zufällige Antwort aus bergruessung
    else:
        if eingabe in verabschiedung:
            return verabschiedung[randrange(len(verabschiedung))]   # Zufällige Antwort aus verabschiedung
        else:
            return "Ich habe Sie nicht verstanden."    # todo Eweiterung mit Liste von Entschuldigungen


def simple_chat_bot():
    eingabe = ""    # ist lokale Variable?
    while eingabe not in verabschiedung:
        eingabe = input()
        antwort = antwort_finden(eingabe)
        print(antwort)
    wegschreiben(verabschiedung, 'verabschiedung.txt')


if __name__ == '__main__':   # Die Konstruktion if __name__ == ”__main__” wird eingesetzt um eine Python Datei als eigenständiges Programm zu nutzen und einzelne Elemente dieser Datei importierbar zu machen.
    simple_chat_bot()
