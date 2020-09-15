def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
       
    for num in rgb:
        if not 0<= num <= 255:
            raise ValueError
            
    r = str(hex(rgb[0]))[2:].upper().zfill(2)
    g = str(hex(rgb[1]))[2:].upper().zfill(2)
    b = str(hex(rgb[2]))[2:].upper().zfill(2)
    
    return f'#{r}{g}{b}'
    pass