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

#Sommerswerd = 'sommerswerd' #schreibt man wirklich so. +8 Kampfstärke, Doppelter Schaden gegen untote. Manchmal als besonderer Gegenstand verwendbar.