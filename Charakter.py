from random import*
#Einsamer Wolf - Band 2
#Kaidisziplinen
#0-Tarnung, 1-Jagt, 2-6.Sinn, 3-Spurensuche, 4-Heilkraft, 5-Waffenstärke, 6-Gedankensperre, 7-Denkstrahl,8-Tierverständnis, 9-Geist_gegen_Materie
#Waffenstärke: 0-Dolch, 1-Speer, 2-Streitkolben, 3-Kurzschwert, 4-Kampfhammer, 5-Schwert, 6-Streitaxt, 7-Schwert, 8-Schlagstock, 9-Breitschwert
from Waffentyp import Waffentyp


class Charakter:
    def __init__(self):
        self.kaifähigkeiten = []
        self.kampfstärke = randint(11,21)
        self.ausdauerpunkte = randint(21,31)
        self.ausdauerpunkte_max = self.ausdauerpunkte
        self.kaidisziplinen_max = 5
        self.rucksack = []
        self.besondere_gegenstände = []
        self.waffen = []
        self.mahlzeiten = 0
        self.tragbeutel = randint(11,21)
        self.kaifähigkeiten.append(Waffentyp.Langschwert)
        self.seitenzahl = 0

waffenstaerke = [0,0,1,0,0,0,0,0,0,0]
kai = [1,1,1,0,1,waffenstaerke,1,0,0,0]

#KAMPFSTÄRKE
kampfstaerke=16
kwolf = kampfstaerke

#AUSDAUER
ausdauer=23


#Waffen: 0-Dolch, 1-Speer, 2-Streitkolben, 3-Kurzschwert, 4-Kampfhammer, 5-Schwert, 6-Streitaxt, 7-Schwert, 8-Schlagstock, 9-Breitschwert
waffen = [0,0,0,0,0,0,0,0,0,0]

#Rucksack
gegenstaende = [] #maximal 8
mahlzeiten = 2

besondere_gegenstände = ['Karte','Schild']
tragbeutel = 13



