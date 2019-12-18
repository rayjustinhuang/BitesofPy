class Animal:

    def __init__(self, name):
        self.animal = name
        animal_list.append(name.title())
        pass

    def __str__(self):
        reference = enumerate(animal_list, 10000)[-1]
        return f"{reference[0]}. {reference[1].title()}"
        pass

    @classmethod
    def zoo(cls):
        return_string = ''
        for animal in enumerate(animal_list, 10000):
            return_string += f"{animal[0]}. {animal[1].title()}\n"
        return return_string[:-1]
        pass