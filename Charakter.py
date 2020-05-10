from random import*
#Einsamer Wolf - Band 2
#Kaidisziplinen
#0-Tarnung, 1-Jagt, 2-6.Sinn, 3-Spurensuche, 4-Heilkraft, 5-Waffenstärke, 6-Gedankensperre, 7-Denkstrahl,8-Tierverständnis, 9-Geist_gegen_Materie
#Waffenstärke: 0-Dolch, 1-Speer, 2-Streitkolben, 3-Kurzschwert, 4-Kampfhammer, 5-Schwert, 6-Streitaxt, 7-Schwert, 8-Schlagstock, 9-Breitschwert
from Waffentyp import Waffentyp


class Charakter:

    # TODO: How do you implement multiple constructors in python? Double check.
    def __init__(self, seitenzahl, kampfstärke, ausdauerpunkte, ausdauerpunkte_max, kaidisziplinen_max, rucksack, besondere_gegenstände, waffen, mahlzeiten, tragbeutel, kaifähigkeiten):
        self.seitenzahl = seitenzahl
        self.kampfstärke = kampfstärke
        self.ausdauerpunkte = ausdauerpunkte
        self.ausdauerpunkte_max = ausdauerpunkte_max
        self.kaidisziplinen_max = kaidisziplinen_max
        self.rucksack = rucksack
        self.besondere_gegenstände = besondere_gegenstände
        self.waffen = waffen
        self.mahlzeiten = mahlzeiten
        self.tragbeutel = tragbeutel

    @classmethod
    def crate_random(cls):
        ausdauerpunkte = randint(21,31)
        return cls(
            seitenzahl = 0,
            kampfstärke = randint(11,21),
            ausdauerpunkte = ausdauerpunkte,
            ausdauerpunkte_max = ausdauerpunkte,
            kaidisziplinen_max = 5,
            rucksack = [],
            besondere_gegenstände = [],
            waffen = [],
            mahlzeiten = 0,
            tragbeutel = randint(11,21),
            kaifähigkeiten = [Waffentyp.Breitschwert]
        )

    @classmethod
    def from_json_dic(cls, character_as_json: str):
        return cls(
            kampfstärke = character_as_json["kampfstärke"],
            ausdauerpunkte = character_as_json["ausdauerpunkte"],
            ausdauerpunkte_max = character_as_json["ausdauerpunkte_max"],
            kaidisziplinen_max = character_as_json["kaidisziplinen_max"],
            rucksack = character_as_json["rucksack"],
            besondere_gegenstände = character_as_json["besondere_gegenstände"],
            waffen = character_as_json["waffen"],
            mahlzeiten = character_as_json["mahlzeiten"],
            tragbeutel = character_as_json["tragbeutel"],
            kaifähigkeiten = list(map(lambda x: Waffentyp[x], character_as_json["kaifähigkeiten"])),
            seitenzahl = character_as_json["seitenzahl"]
        )



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



