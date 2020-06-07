import json
from random import*
from Armory import *

#Einsamer Wolf - Band 2
#Kaidisziplinen
#0-Tarnung, 1-Jagt, 2-6.Sinn, 3-Spurensuche, 4-Heilkraft, 5-Waffenstärke, 6-Gedankensperre, 7-Denkstrahl,8-Tierverständnis, 9-Geist_gegen_Materie
#Waffenstärke: 0-Dolch, 1-Speer, 2-Streitkolben, 3-Kurzschwert, 4-Kampfhammer, 5-Schwert, 6-Streitaxt, 7-Schwert, 8-Schlagstock, 9-Breitschwert

@dataclass()
class Charakter:
    head: Equippable
    body: Equippable
    main_hand: Weapon
    off_hand: Equippable
    page: int
    fighting_power: int
    endurance_points: int
    endurance_points_max: int
    kai_discipline_max: int
    food_rations: int
    wallet: int
    backpack: []
    special_items: []
    kai_disciplines: []

    @classmethod
    def crate_random(cls):
        ausdauerpunkte = randint(21,31)
        return cls(
            head = Helm,
            body = None,
            main_hand = Weapon(BodyPart.MainHand, 2, 0, WeaponType.Broadsword),
            off_hand= None,
            page = 0,
            fighting_power = randint(11,21),
            endurance_points = ausdauerpunkte,
            endurance_points_max = ausdauerpunkte,
            kai_discipline_max = 5,
            food_rations = 0,
            wallet = randint(11,21),
            backpack = [],
            special_items = [],
            kai_disciplines = []
        )

    @classmethod
    def from_json(cls, character_as_json: str):
        return cls(
            head = character_as_json['head'],
            body = character_as_json['body'],
            main_hand = character_as_json['main_hand'],
            off_hand= character_as_json['off_hand'],
            page = character_as_json["page"],
            fighting_power = character_as_json["fighting_power"],
            endurance_points = character_as_json["endurance_points"],
            endurance_points_max = character_as_json["endurance_points_max"],
            kai_discipline_max = character_as_json["kai_discipline_max"],
            food_rations = character_as_json["food_rations"],
            wallet = character_as_json["wallet"],
            backpack = character_as_json["backpack"],
            special_items = character_as_json["special_items"],
            kai_disciplines = list(map(lambda x: WeaponType[x], character_as_json["kai_disciplines"])),
        )

    def to_json(self):
        def convert(o):
            try:
                if(isinstance(o, Enum)):
                    return o.value
                return o.__dict__
            except:
                return None

        return json.dumps(self, default=convert, indent=4, ensure_ascii=False)


#TODO: I don't get this.
waffenstaerke = [0,0,1,0,0,0,0,0,0,0]
kai = [1,1,1,0,1,waffenstaerke,1,0,0,0]

#KAMPFSTÄRKE
# kampfstaerke=16
# kwolf = kampfstaerke

#AUSDAUER
ausdauer=23


#Waffen: 0-Dolch, 1-Speer, 2-Streitkolben, 3-Kurzschwert, 4-Kampfhammer, 5-Schwert, 6-Streitaxt, 7-Schwert, 8-Schlagstock, 9-Breitschwert
# waffen = [0,0,0,0,0,0,0,0,0,0]

#Rucksack
# gegenstaende = [] #maximal 8
# mahlzeiten = 2

# besondere_gegenstände = ['Karte','Schild']
# tragbeutel = 13



