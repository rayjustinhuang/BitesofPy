from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    def __init__(self, id_name, name, max_level, description, items=[]):
        self.id_name = id_name
        self.name = name
        reg_num_level_dict = dict(zip('I II III IV V VI VII VIII IX X'.split(), [1,2,3,4,5,6,7,8,9,10]))
        if type(max_level) == int:
            self.max_level = max_level
        else:
            self.max_level = reg_num_level_dict[max_level]
        self.description = description
        self.items = items
    
    def __str__(self):
        name_to_use = self.name.title()
        num_level = self.max_level
        return f'{name_to_use} ({num_level}): {self.description}'
    
    def items(self):
        return self.items
    pass


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    def __init__(self, name, enchantments=[]):
        self.name = name.replace("_", " ")
        self.enchantments = list(enchantments)
        
    def __str__(self):
        final_string = f'{self.name.title()}: \n'
        for e in sorted(self.enchantments, key=lambda x: x.id_name):
            name_to_use = e.id_name.replace(' ',"_").lower()
            num_level = e.max_level
            final_string += f'  [{num_level}] {name_to_use}\n'
        return final_string[:-1]
    pass

def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    def extract_items(string):
        new_string = string.split('/')[-1].split('.')[0]
        replacements = (('enchanted',''), ('iron',''), ('sm',''), ('fishing_rod', 'fishing rod'))
    
        for r in replacements:
            new_string = new_string.replace(*r)
    
        item_list = ['fishing_rod' if item == 'fishing rod' else item for item in new_string.split("_")]
        item_list = list(filter(None,item_list))
    
        return item_list

    enchantment_dict = defaultdict(Enchantment)
    enchantment_table = soup.find('table', id='minecraft_items')
    enchantment_table_data = enchantment_table.find_all('tr')
    for row in enchantment_table_data[1:]:
        #print(row)
        name = row.find('a').text
        #print(name)
        id_name = row.find('em').text
        #print(id_name)
        max_level = row.find_next('td').find_next('td').text
        #print(max_level)
        description = row.find('td', class_='hidden-xs').text
        #print(description)
        items = extract_items(row.find('img', class_='img-rounded')['data-src'])
        #print(items)
        entry = (id_name, name, max_level, description, items)
        enchantment_dict[id_name] = Enchantment(*entry)
        #print('-------------------------------')
    return enchantment_dict
    pass


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    item_flat_dict = defaultdict(list)
    item_dict = defaultdict(Item)
    
    for enchantment in data:
        for item in data[enchantment].items:
            item_flat_dict[item].append(data[enchantment])
    
    for item in sorted(item_flat_dict.keys()):
        item_dict[item] = Item(item, item_flat_dict[item])
        
    return item_dict
    pass


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup
soup = get_soup()
enchantment_data = generate_enchantments(soup)
#print(enchantment_data['mending'].max_level)
item_data = generate_items(enchantment_data)
print(item_data['armor'].enchantments[0].id_name)

def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


#if __name__ == "__main__":
#    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""