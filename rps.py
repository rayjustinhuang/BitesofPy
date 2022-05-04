from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    moves = defeated_by.values()
    return random.choice(moves)
    pass


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if player_choice == defeated_by[computer_choice]:
        return win.format(player_choice, computer_choice)
    elif player_choice == computer_choice:
        return tie
    else:
        return lose.format(player_choice, computer_choice)
    pass


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    player_choice = yield
    computer_choice = _get_computer_move()
    
    while player_choice != 'q':
        print(_get_winner(computer_choice, player_choice))
        
    raise StopIteration
    pass

#print(_get_winner('rock', 'paper'))