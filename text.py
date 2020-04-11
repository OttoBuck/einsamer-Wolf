from Kampf import*
from Aktionsblatt import*
from Definitionen import*

page = [
    [["Du entdeckst eine Leiche. \n Willst du sie durchsuchen, lies weiter bei 1 \n willst du weiter entlang des Pfades gehen, lies weiter bei 2"]],    #pg 0
    #pg 1
        [["Beim durchsuchen entdeckst du ein Kettenhemd",'Kettenhemd',besondere_gegenstände, "Lies weiter bei 3"]],
    #pg2
        [["Du siehst eine Gestalt in der Ferne."],
            [[1,"Willst du dich tarnen und im Unterholz verstecken, lies weiter bei 6"],[0],
            [1,"Willst du deinen 6. Sinn anwenden, lies weiter bei 5"],[0],[0],[0],[0],[0],[0],[0]],
         ["Willst du zu ihr gehen und Hallo sagen? Lies weiter bei 3"]], #0-Tarnung, 1-Jagt, 2-6.Sinn, 3-Spurensuche, 4-Heilkraft, 5-Waffenstärke, 6-Gedankensperre, 7-Denkstrahl,8-Tierverständnis, 9-Geist_gegen_Materie
    #pg3
        [["Die Person greift dich an."],[18,22,0,0,1], ["du gehts glücklich weiter"]],
    #pg4
        [["Du gehst glücklich weiter" ],
    #pg 5
        ["Dein 6. Sinn schlägt alarm"]
         ]
]





ks_wolf = kampfstaerke + waffenboni(waffen,waffenstaerke)+ bes_geg_boni()[0]
ausdauer_wolf = ausdauer



def read (number,ausdauer_wolf):
    for i in page[number]:
        if len(i) == 1: #text
            print (i[0])
        if len(i) == 10: #Kai fertigkeiten
            zaehler = 0
            for faehigkeit in i:
                if faehigkeit[0] == 1 and kai[zaehler] != 0:
                    print(faehigkeit[1])
        if len(i)==4:#gegenstand
            print(i[0])
            if input("willst du diesen Gegenstand aufheben?") == "Ja":
                i[2][0:0]=[i[1]]
                print("Besondere Gegenstände: ", i[2])
        if len(i)==5: #kampf
            print("KAMPFSTÄRKE ", i[0]," AUSDAUER ",i[1])
            if kai[6] == 0:
                if i[2] == 1:
                    print("Der Gegner verfügt über Denkstrahl!")
            if i[3] == 1:
                if kai[7]==1:
                    print("Der Gegner ist immun gegen Denkstrahl!")
            ausdauer_wolf = fight(i[0], i[1], i[2], i[3], i[4], ausdauer_wolf, ks_wolf)
    return ausdauer_wolf




while 1:
    ausdauer_wolf= read(eval(input()),ausdauer_wolf)
    if kai[4] == 1:
        if ausdauer_wolf < (ausdauer + bes_geg_boni()[1]):
            ausdauer_wolf += 1


