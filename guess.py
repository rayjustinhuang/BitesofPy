import random
MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False
        pass

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        
        usernumber = input(f'Guess a number between {START} and {END}: ')
        
        if usernumber == "" or usernumber == None:
            raise ValueError('Please enter a number')
        
        try:
            usernumber = int(usernumber)
        except:
            raise ValueError('Should be a number')
            
        usernumber = int(usernumber)
        
        if usernumber < START or usernumber > END:
            raise ValueError('Number not in range')
        elif usernumber in self._guesses:
            raise ValueError('Already guessed')
        else:
            self._guesses.add(usernumber)
            return usernumber

        pass

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
           
        if self._answer == guess:
            print(f'{guess} is correct!')
            self._win = True
            return True
        elif self._answer < guess:
            print(f'{guess} is too high')
            return False
        else:
            print(f'{guess} is too low')
            return False
        pass

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        
        counter, result = 0, False
        
        while self._win == False:
            while True:
                try:
                    guess = self.guess()
                    break
                except ValueError as err:
                    print(err)

            counter += 1
            self._win = self._validate_guess(guess)
            

            if counter == 5:
                print(f'Guessed 5 times, answer was {self._answer}', end="")
                break
            
        pass


if __name__ == '__main__':
    game = Game()
    game()