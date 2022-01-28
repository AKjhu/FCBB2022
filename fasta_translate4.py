import sys
import math

# Create codon translation dictionary using hard_codon_table.txt
codon_text = open("codon_table_hard.txt", "r")
Codon_Dict = {}
for line in codon_text:
    temp_amino_acid = line.split()[1]
    temp_codons_list = line.split()[2]
    temp_num_codons = math.ceil(len(temp_codons_list) / 4)
    i = 0
    for c in range(0, temp_num_codons):
        temp_codon = temp_codons_list[i:i+3]
        Codon_Dict[temp_codon] = temp_amino_acid
        i += 4

# Create a dictionary of descriptor_str and sequence_str pairs
Genes_Dict = {}
temp_descriptor_str = ''
temp_sequence_str = ''
# Fill Genes_Dict with genes
for line in sys.stdin:
    # If we hit a new gene or the end of file, update Genes_Dict
    if (line[0] == '>'):
        if (temp_sequence_str != ''):
            Genes_Dict[temp_descriptor_str] = temp_sequence_str
        temp_descriptor_str = str.strip(line)
        temp_sequence_str = ''
    else:
        temp_sequence_str += str.strip(line)
# Once we reach the end of the file, enter last gene pair
Genes_Dict[temp_descriptor_str] = temp_sequence_str

# Method that translates a sequence_str to amino acids
def translate_sequence(sequence_str):
    # Translate sequence_str into amino acids
    translation_str = ''
    sequence_len = len(sequence_str)
    for i in range(0, sequence_len, 3):
        #Stay within sesquence bounds
        if ((i + 3) > sequence_len):
            break
        temp_codon = sequence_str[i:i+3]
        # Only translate if temp_codon is valid
        if (temp_codon.find('X') == -1):
            translation_str += Codon_Dict[temp_codon]
    return translation_str

# Translate and print each gene in Genes_Dict
for descriptor_str in Genes_Dict: 
    sys.stdout.write(descriptor_str + '\n' + translate_sequence(Genes_Dict[descriptor_str]) + '\n')
    #sys.stdout.write(translate_sequence(Genes_Dict[descriptor_str]))