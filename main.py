# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
# def print_list(list):
#      for begruessung in list:
#          print(begruessung)
#todo Groß- und Kleinschreibung sollte nur bei "eingabe" uninteressant sein
def antwort_finden(eingabe):
    if eingabe == "Hallo":   #todo Eweiterung mit Liste von Begrüßungen
        return "Hey"    #todo Eweiterung mit Liste von Begrüßungen
    else:
        return "Ich verstehe Sie nicht."    #todo Eweiterung mit Liste von Entschuldigungen

def simple_chat_bot():
    eingabe = ""    #ist lokale Variable?
    verabschiedung = ['Tschüss', 'Bye', 'Auf Wiedersehen']
    while eingabe not in (verabschiedung):   #Erweiterung mit Liste von Verabschiedungen ist erledigt
        eingabe = input()
        antwort = antwort_finden(eingabe)
        print(antwort)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #                0       1      2
    # begruessen = ['hello', 'hi', 'hallo']  # hey
    # # begruessen.append('hey')
    # begruessen.insert(0, 'hey')
    # begruessen.sort()
    # print_list(begruessen)
    # input1 = input() # Eingabe mit input()
    # print(input1)    # Ausgabe mit print()
    simple_chat_bot()
