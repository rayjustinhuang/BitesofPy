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
    
    
    
    return output
    pass

bite_15_en = '''<p>Iterate over the given <code>names</code> and <code>countries list</code>s, <strong>printing</strong> them prepending the number of the loop (starting at 1). Here is the output you need to deliver:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Notice that the 2nd column should have a fixed width of 11 chars, so between <i>Julian</i> and <i>Australia</i> there are 5 spaces, between <i>Bob</i> and <i>Spain</i>, there are 8. This column should also be aligned to the left.</p><p>Ideally you use only one for loop, but that is not a requirement.</p><p>Good luck and keep calm and code in Python!</p>'''
bite_15_it = '''<p>Iterare i <code>nomi</code> e le <code>liste dei paesi</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre> 1. Julian Australia 2. Bob Spagna 3. PyBites Global 4. Dante Argentina 5. Martin Stati Uniti d'America 6. Rodolfo Messico </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non � un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''
bite_15_it_fixed = '''<p>Iterare i <code>names</code> e le <code>countries list</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non � un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''

#print(fix_translation(bite_15_en, bite_15_it))