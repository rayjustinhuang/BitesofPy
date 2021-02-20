WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(int(size/2)):
        sequence = [WHITE, BLACK]*int(size/2)
        print("".join(sequence))
        print("".join(sequence[::-1]))
    pass