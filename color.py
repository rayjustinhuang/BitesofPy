import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        if color.upper() in COLOR_NAMES:
            self.rgb = COLOR_NAMES[color.upper()]
        else:
            self.rgb = None
        pass

    @staticmethod
    def hex2rgb(hexcolor):
        """Class method that converts a hex value into an rgb one"""
        if type(hexcolor) != str:
            raise ValueError
        
        def convert_to_dec(string):
            string = string[1:]
            dec_mapping = dict(zip('a b c d e f'.split(),[10,11,12,13,14,15]))
            interim_list = []
            for hex_digit in string:
                try:
                    interim_list.append(int(hex_digit[0]))
                except:
                    interim_list.append(dec_mapping[hex_digit[0]])
    
            split_string = [interim_list[i:i+2] for i in range(0,6,2)]
            return_list = []
    
            for code in split_string:
                return_list.append(int(code[0])*16 + int(code[1]))
                
            return tuple(return_list)
            
        return convert_to_dec(hexcolor)
        pass

    @staticmethod
    def rgb2hex(rgbcode):
        """Class method that converts an rgb value into a hex one"""
        if type(rgbcode) != tuple:
            raise ValueError
        
        def convert_to_hex(number):
            first_digit = int(number/16)
            second_digit = number%16
            hex_mapping = dict(zip(range(10,16), 'a b c d e f'.split()))
            return_str = str()
            for number in (first_digit, second_digit):
                if number > 9:
                    return_str += hex_mapping[number]
                else:
                    return_str += str(number)
            return return_str
        
        final_string = '#'
        for number in rgbcode:
            final_string += convert_to_hex(number)
        
        return final_string
        pass

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"
        pass

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb:
            return str(self.rgb)
        else:
            return 'Unknown'
        pass
    
#c = Color('white')
#print(c.rgb)
#print(c.rgb2hex((0, 0, 255)))
#print(c.hex2rgb('#0000ff'))
#print(repr(c))