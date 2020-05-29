from enum import Enum

class Waffentyp(str, Enum):
    Dolch= 'dolch'
    Speer= 'speer'
    Streitkolben = 'streitkolben'
    Kurzschwert= 'kurzschwert'
    Kampfhammer= 'kampfhammer'
    Schwert= 'schwert'
    Streitaxt= 'streitaxt'
    Schlagstock= 'schlagstock'
    Breitschwert = 'breitschwert'




class Ausrüstung:
    def __init__(self, ort, rüstung_kampfstärke, rüstung_ausdauer):
        self.ort = ort #körper, kopf, haupthand, nebenhand: wie mache ich das ohne string
        self.rüstung_kampfstärke = rüstung_kampfstärke
        self.rüstung_ausdauer = rüstung_ausdauer
    #TODO kann ich die Rüstungsobjekte in der klasse selbst definieren (wie in der Enum-klasse)?
    #TODO oder muss ich diese separat auflisten

Kettenhemd = Ausrüstung("Körper", 0, 4)
Lederhemd = Ausrüstung("Körper", 0, 4)
Helm = Ausrüstung("Kopf", 2, 0)
Schild = Ausrüstung("nebenhand", 2, 0)


#class Rüstung:(Rüstung, Enum) funzt so nicht
#    Kettenhemd= ("körper", 0, 4)



#Sommerswerd = 'sommerswerd' #schreibt man wirklich so. +8 Kampfstärke, Doppelter Schaden gegen untote. Manchmal als besonderer Gegenstand verwendbar.