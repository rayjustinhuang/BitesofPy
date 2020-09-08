INDENTS = 4


def print_hanging_indents(poem):
    
    split_poem = poem.strip().splitlines()
    
    length = len(split_poem)
    
    for i in range(length):
        if i == 0:
            print(split_poem[i].strip())
        elif split_poem[i] == "":
            continue
        elif split_poem[i-1].strip() != "":
            #print(split_poem[i+1].strip())
            print("    "+split_poem[i].strip())
        else:
            print(split_poem[i].strip())
    pass