cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ", ".join(cars['Jeep'])
    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    output_list = [cars[brand][0] for brand in cars]
    return output_list
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    output_list = []
    
    for brand in cars:
        for model in cars[brand]:
            if grep.lower() in model.lower():
                output_list.append(model)
    
    return sorted(output_list)
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_cars = cars.copy()
    for brand in sorted_cars:
        sorted_cars[brand] = sorted(sorted_cars[brand])
    
    return sorted_cars
    pass