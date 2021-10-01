def get_profile(name, age: int, *sports, **awards):
    if type(age) != int:
        raise ValueError
    if len(sports) > 5:
        raise ValueError
    
    return {'name': name, 'age': age, 'sports': sports, 'awards': awards}
    pass