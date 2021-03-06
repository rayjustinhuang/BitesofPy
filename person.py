# see __mro__ output in Bite description

class Person:
    def __init__(self):
        pass
    
    def __repr__(self, string=""):
        return "I am a person" + string

class Mother(Person):
    
    def __str__(self):
        return self.__repr__(" and awesome mom")
                
class Father(Person):
    
    def __str__(self):
        return self.__repr__(" and cool daddy")
        
class Child(Father, Mother):
    
    def __str__(self):
        return 'I am the coolest kid'