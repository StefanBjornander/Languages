import Uppgift9_1

while True:
    hand1 = Uppgift9_1.sten_sax_pase()
    hand2 = Uppgift9_1.sten_sax_pase()
    print('Spelare 1', hand1);
    print('Spelare 2', hand2);

    resultat = Uppgift9_1.play(hand1, hand2);
    if resultat == -1:
        print('Spelare 1 vann');
    elif resultat == 1:
        print('Spelare 2 vann');
    else:
        print('Oavgjort');

    svar = input('Vill du spela igen? ')
    if (svar.lower() == 'nej'):
        break