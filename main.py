import pickle as p  # wird eventuell wieder entfernt
from antwort_finden import antwort_finden
# from random import randrange

# Variablen die in mehreren Bereichen genutzt werden


def wegschreiben(liste, dateiname):    # todo auf JSON ansehen
    with open(dateiname, 'wb') as tmp:
        p.dump(liste, tmp)
# def einlesen(dateiname, liste):
# with open(dateiname, 'rb') as tmp:
# liste = p.load(tmp)


def simple_chat_bot():
    verabschiedung = ['']
    eingabe = ""  # ist lokale Variable?
    while eingabe not in (verab.lower() for verab in verabschiedung):
        eingabe = input()
        antwort = antwort_finden(eingabe)
        print(antwort)
    # todo intents.json wegschreiben


if __name__ == '__main__':
    simple_chat_bot()
