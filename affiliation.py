def generate_affiliation_link(url):
    split_link = url.split('dp/')
    
    raw_id = split_link[-1]
    
    clean_id = raw_id.split('/')[0]
    
    return f'http://www.amazon.com/dp/{clean_id}/?tag=pyb0f-20'