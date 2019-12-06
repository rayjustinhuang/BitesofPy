from pathlib import Path
from urllib.request import urlretrieve

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
    def __init__(self, id_name, name, max_level, description, items):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items
    
    def __repr__(self):
        name_to_use = self.name.title()
        reg_num_level_dict = dict(zip('I II III IV V'.split(), [1,2,3,4,5]))
        num_level = reg_num_level_dict[self.max_level]
        return f'{name_to_use} ({num_level}): {self.description}'
    
    def items(self):
        return self.items
    pass


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    def __init__(self, name, enchantments):
        self.name = name.replace("_", " ").title()
        self.enchantments = enchantments
        reg_num_level_dict = dict(zip('I II III IV V'.split(), [1,2,3,4,5]))
        
    def __repr__(self):
        final_string = f'{self.name}\n'
        for e in self.enchantments:
            name_to_use = e.name.replace(' ',"_").lower()
            num_level = reg_num_level_dict[e.max_level]
            final_string += f' [{num_level}] {name_to_use}\n'
    pass


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    enchantment_dict = defaultdict(Enchantment)
    enchantment_table = soup.find('table', id='minecraft_items')
    for row in enchantment_table:
        name = row.find('a').text
        id_name = row.find('em').text
        max_level = row.find('td').text
        description = row.find('td', class_='hidden-xs').text
        items = row.find('img')['src'].split('/')[-1].split('.')[0].split("_")
        entry = (id_name, name, max_level, description, items)
        enchantment_dict[id_name].add(*entry)
    pass


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    
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


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

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