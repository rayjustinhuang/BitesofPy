import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    
    pre_tag = re.compile(r'<pre>[\S\s]*<\/pre>')
    
    translated_pre = re.findall(pre_tag, org_text)
    
    #print(translated_portion_to_copy[0])
    
    replace_pre = re.sub(pre_tag, translated_pre[0], trans_text)
    
    code_tag = re.compile(r'<code>[\S\s]*?<\/code>')
    
    translated_code = re.findall(code_tag, trans_text)
    original_code = re.findall(code_tag, org_text)
    
    split_by_code = re.split(code_tag, replace_pre)
    
    final_output = [None]*(len(split_by_code)+len(original_code))
    
    final_output[::2] = split_by_code
    final_output[1::2] = original_code
    
    return "".join(final_output)
    pass