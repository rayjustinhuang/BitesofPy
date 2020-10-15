import os
from urllib.request import urlretrieve
import collections

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    table = []
    
    table.append('|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |')
    
    formatted_translation_table = {}
    
    for line in translation_table_str.splitlines():
        pair = line.split(' = ')
        
        if len(pair) == 2:
            key = pair[0].strip()
            value = pair[1].strip()
        
            formatted_translation_table[key] = value
    
    formatted_translation_table['Base1'] = formatted_translation_table['Base1'].replace('T','U')
    formatted_translation_table['Base2'] = formatted_translation_table['Base2'].replace('T','U')
    formatted_translation_table['Base3'] = formatted_translation_table['Base3'].replace('T','U')
    
    print(formatted_translation_table)
    
    joined_sequences = "".join(sequences)
    
    base_len = len(joined_sequences) - 2
    
    codon = collections.namedtuple('Codon', ['name', 'AA', 'freq', 'count'])
    
    translation_tuples = []
    
    for i in range(len(formatted_translation_table['AAs'])):
        name = formatted_translation_table['Base1'][i] + formatted_translation_table['Base2'][i] + formatted_translation_table['Base3'][i]
        AA = formatted_translation_table['AAs'][i]
        count = joined_sequences.count(name)
        freq = count/base_len
        translation_tuples.append(codon(name, AA, freq, count))

    print(translation_tuples)    
    pass


if __name__ == "__main__":
    print(return_codon_usage_table())