import json

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""

def replace_noncommas(string):
    replacements = ((';',','), ('|',','))
    
    for r in replacements:
        string = string.replace(*r)
        
    return string


def convert_to_json(members=members):
    new_members = []
    for row in members.splitlines():
        if row != "":
            new_members.append(replace_noncommas(row))
        
    json_output = []   
    keys = new_members[0].split(',')
    for row in new_members[1:]:
        json_output.append(dict(zip(keys, row.split(','))))
        
    return json.dumps(json_output)
    pass