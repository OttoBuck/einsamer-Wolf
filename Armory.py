from Waffentyp import*

class Armory:
    def __init__(self, kopf, körper, haupthand, nebenhand):
        self.kopf = kopf
        self.körper = körper
        self.haupthand = haupthand # Waffe aus Waffentyp (Falls leer: Kampfstärke -= 4)
        self.nebenhand = nebenhand # Waffe aus Waffentyp oder Schild
