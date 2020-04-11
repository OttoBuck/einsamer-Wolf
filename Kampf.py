from random import*
from Aktionsblatt import*


ka0 = [(0,99),[0,99],[0,8],[0,8],[1,7],[2,6],[3,5],[4,4],[5,3],[6,0]] #-11-
ka1 = [[0,99],[0,8],[0,7],[1,7],[2,6],[3,6],[4,5],[5,4],[6,3],[7,0]] #-10/9
ka2 = [[0,8],[0,7],[1,6],[2,6],[3,5],[4,5],[5,4],[6,3],[7,2],[8,0]] #-8/7
ka3 = [[0,6],[1,6],[2,5],[3,5],[4,4],[5,4],[6,3],[7,2],[8,0],[9,0]] #-6/5
ka4 = [[1,6],[2,5],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1],[9,0],[10,0]] #-4/3
ka5 = [[2,5],[3,5],[4,4],[5,4],[6,3],[7,2],[8,2],[9,1],[10,0],[11,0]] #-2/1
ka6 = [[3,5],[4,4],[5,4],[6,3],[7,2],[8,2],[9,1],[10,0],[11,0],[12,0]] #0
ka7 = [[4,5],[5,4],[6,3],[7,3],[8,2],[9,2],[10,1],[11,0],[12,0],[14,0]] #1/2
ka8 = [[5,4],[6,3],[7,3],[8,2],[9,2],[10,2],[11,1],[12,0],[14,0],[16,0]] #3/4
ka9 = [[6,4],[7,3],[8,3],[9,2],[10,2],[11,1],[12,0],[14,0],[16,0],[18,0]] #5/6
ka10 = [[7,4],[8,3],[9,2],[10,2],[11,2],[12,1],[14,0],[16,0],[18,0],[99,0]] #7/8
ka11 = [[8,3],[9,3],[10,2],[11,2],[12,2],[14,1],[16,0],[18,0],[99,0],[99,0]] #9/10
ka12 = [[9,3],[10,2],[11,2],[12,2],[14,1],[16,1],[18,0],[99,0],[99,0],[99,0]] #11+
listk = [ka0, ka1, ka2, ka3, ka4, ka5, ka6, ka7, ka8, ka9, ka10, ka11, ka12]
def fight(ksf,apf,dsf,gsf,run,ausdauer_wolf,ks_wolf): #kampfstärke, ausdauer, denkstrahl, gedankensperre, nach wie vielen runden wegrennen? ausdauer_wolf, Kampfstärke_wolf
    if dsf == 1:
        if kai[6] == 0:
            ksf += 2
    if kai[7] == 1:
        if[gsf]==0:
            ksf -= 2
    ks_wolf = 14
    kampfquotient = ks_wolf - ksf
    kax, kay= 0,-11
    while 1:
        if kampfquotient <= kay:
            break
        else:
            kax += 1
            kay += 2
    runde=1
    kampf = True
    while kampf is True:
        zufall = randint(0, 9)
        print("Runde", runde, " Du hast noch ", ausdauer_wolf, " Ausdauer. Dein Gegner hat ", apf," Ausdauer. Der Kampfquotient liegt bei ", kay)
        if runde > run:
            if input( "Willst du wegrennen? Ja/Nein")=="Ja":
                ausdauer_wolf -= listk[kax][zufall][1]
                return ausdauer_wolf
        ausdauer_wolf -= listk[kax][zufall][1]
        if ausdauer_wolf <= 0:
            print ("Du bist gestorben")
            exit()
            return ausdauer_wolf
        apf -= listk[kax][zufall][0]
        print("Du hast eine ", zufall, " gewürfelt: Ausdauer Wolf -",listk[kax][zufall][1], ", Ausdauer Feind -", listk[kax][zufall][0])
        if apf <= 0:
            print("Runde", runde, " Du hast noch ", ausdauer_wolf, " Ausdauer. Dein Gegner ist gestorben.")
            return ausdauer_wolf
        runde += 1

