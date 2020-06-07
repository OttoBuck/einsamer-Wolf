from dataclasses import dataclass
from enum import Enum

class BodyPart(Enum):
    Chest = 1
    Head = 2
    MainHand = 3
    OffHand = 4

class WeaponType(Enum):
    Dagger = 1
    Speer = 2
    Mace = 3
    ShortSword = 4
    WarHammer = 5
    Sword= 6
    BattleAx= 7
    Quarterstaff= 8
    Broadsword = 9


@dataclass
class Equippable:
    slot: BodyPart
    fighting_power: int
    endurance_points: int
    #TODO kann ich die Rüstungsobjekte in der klasse selbst definieren (wie in der Enum-klasse)?
    #TODO oder muss ich diese separat auflisten


@dataclass()
class Weapon(Equippable):
    weapon_type: WeaponType


#TODO: we can expose the items like this, but I'd prefere it, if the page that gives you an item also creates it.
Kettenhemd = Equippable(BodyPart.Chest, 0, 4)
Lederhemd = Equippable(BodyPart.Chest, 0, 4)
Helm = Equippable(BodyPart.Head, 2, 0)
Schild = Equippable(BodyPart.OffHand, 2, 0)  # TODO: are there any weapons which require two slots? Can every weapon, that can be wielded in mainhand also be wielded in offhand?


#class Rüstung:(Rüstung, Enum) funzt so nicht
#    Kettenhemd= ("körper", 0, 4)



#Sommerswerd = 'sommerswerd' #schreibt man wirklich so. +8 Kampfstärke, Doppelter Schaden gegen untote. Manchmal als besonderer Gegenstand verwendbar.
