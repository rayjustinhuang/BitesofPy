IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    output_list = []
    for name in names:
        if name[0] == IGNORE_CHAR:
            continue
        if any(i.isdigit() for i in name):
            continue
        if name[0] == QUIT_CHAR:
            break
        if len(output_list) == MAX_NAMES:
            break
        output_list.append(name)
    
    return output_list
    pass