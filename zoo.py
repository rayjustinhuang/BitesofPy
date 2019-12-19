class Animal:
    animal_list = list()

    def __init__(self, name):
        self.animal = name
        Animal.animal_list.append(self.animal)
        pass

    def __str__(self):
        reference = list(enumerate(Animal.animal_list, 10001))[-1]
        return f"{reference[0]}. {reference[1].title()}"
        pass

    @classmethod
    def zoo(cls):
        return_string = ''
        for animal in enumerate(Animal.animal_list, 10001):
            return_string += f"{animal[0]}. {animal[1].title()}\n"
        return return_string[:-1]
        pass