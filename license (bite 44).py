import string, secrets
alphabet = string.ascii_uppercase + string.digits

def gen_key(parts=4, chars_per_part=8):
    result_key = '-'.join([''.join(secrets.choice(alphabet) for i in range(chars_per_part)) for _ in range(parts)])

    return result_key