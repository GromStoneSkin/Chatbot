from random import randrange


def antwort_finden(eingabe):  # Groß- und Kleinschreibung sollte bei "eingabe" uninteressant sein
    begruessung = ['']
    verabschiedung = ['']
    if eingabe.lower() in (begr.lower() for begr in begruessung):
        return begruessung[randrange(len(begruessung))]  # Zufällige Antwort aus bergruessung
    else:
        if eingabe in (verab.lower() for verab in verabschiedung):
            return verabschiedung[randrange(len(verabschiedung))]  # Zufällige Antwort aus verabschiedung
        else:
            return "Ich habe Sie nicht verstanden."  # todo Eweiterung mit Liste von Entschuldigungen


if __name__ == '__antwort_finden__':
    antwort_finden(eingabe='')
