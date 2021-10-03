def get_profile(name, age: int, *sports, **awards):
    if type(age) != int:
        raise ValueError
    if len(sports) > 5:
        raise ValueError
        
    if sports and not awards:
        sports = sorted(list(sports))
        return {'name': name, 'age': age, 'sports': sports}
    
    if not sports and awards:
        return {'name': name, 'age': age, 'awards': awards}
        
    if not sports and not awards:
        return {'name': name, 'age': age}
        
    return {'name': name, 'age': age, 'sports': sports, 'awards': awards}
    pass