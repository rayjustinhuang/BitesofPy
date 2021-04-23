def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        n = len(list(data.items())[0])
    else:
        n = len(data[0])
    
    outputs = [[] for i in range(n)]
    
    if type(data) == dict:
        for item in data.items():
            for i in range(n):
                outputs[i].append(item[i])
    else:
        for item in data:
            for i in range(n):
                outputs[i].append(item[i])
                
    outputs = [tuple(i) for i in outputs]
    
    return outputs
    