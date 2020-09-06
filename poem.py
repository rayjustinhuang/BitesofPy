INDENTS = 4


def print_hanging_indents(poem):
    
    split_poem = poem.strip().splitlines()
    
    for i in range(len(split_poem)):
        if i == len(split_poem)-1:
            print('    '+split_poem[i].strip())
        elif split_poem[i] == "":
            continue
        elif split_poem[i+1].strip() != "":
            print(split_poem[i].strip())
        else:
            print("    "+split_poem[i].strip())
    pass

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

#print_hanging_indents(shakespeare_unformatted)

"""
        try:
            if split_poem[i+1] != "":
                print(split_poem[i].strip())
            else:
                print("    "+split_poem[i].strip())
        except:
            print('    '+split_poem[i].strip())
"""