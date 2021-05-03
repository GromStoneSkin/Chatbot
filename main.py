# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
# def print_list(list):
#      for begruessung in list:
#          print(begruessung)

# todo Groß- und Kleinschreibung sollte bei "eingabe" uninteressant sein
from random import randrange


def antwort_finden(eingabe):
    begruessung = ['Hallo', 'Hey', 'Guten Tag', 'Hi', 'Moin']
    if eingabe in begruessung:
        return begruessung[randrange(len(begruessung))]   # Zufällige Antwort
    else:
        return "Ich habe Sie nicht verstanden."    # todo Eweiterung mit Liste von Entschuldigungen


def simple_chat_bot():
    eingabe = ""    # ist lokale Variable?
    verabschiedung = ['Tschüss', 'Bye', 'Auf Wiedersehen']
    while eingabe not in verabschiedung:
        eingabe = input()
        antwort = antwort_finden(eingabe)
        print(antwort)


if __name__ == '__main__':   # Die Konstruktion if __name__ == ”__main__” wird eingesetzt um eine Python Datei als eigenständiges Programm zu nutzen und einzelne Elemente dieser Datei importierbar zu machen.

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
    simple_chat_bot()
