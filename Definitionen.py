from Aktionsblatt import*



def waffenboni (waffen, waffenstaerke):
    if sum(waffen) == 0:
        return -4
    zaeler = 0
    for i in waffen:
        if i == 1:
            if waffenstaerke[zaeler] == 1:
                return 2
        zaeler += 1
        if zaeler == 10:
            return 0

def bes_geg_boni():
    ks_bg = 0
    a_bg = 0
    for i in besondere_gegenstände:
        if i == 'Schild':
            ks_bg += 2
        if i == 'Kettenhemd':
            a_bg += 4
    return [ks_bg, a_bg]


