import csv
import os
from urllib.request import urlretrieve

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = dict()
    
    with open(BATTLE_DATA) as f:
        csv_reader = csv.DictReader(f)
        
        for row in csv_reader:
            defeat_mapping[row['Attacker']] = [keys for keys, values in row.items() if values == 'win']
    
    return defeat_mapping
    pass


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    # ...
    if player1 not in defeat_mapping.keys() or player2 not in defeat_mapping.keys():
        raise ValueError('Invalid player string/s passed')
    
    if player1 == player2:
        return 'Tie'
    elif player2 in defeat_mapping[player1] and player1 in defeat_mapping[player2]:
        return 'Tie'
    elif player2 in defeat_mapping[player1] and not player1 in defeat_mapping[player2]:
        return player1
    else:
        return player2