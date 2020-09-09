def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    
    tran_table = str.maketrans('','', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    output_string = input_string.translate(tran_table)
    
    return output_string
    pass