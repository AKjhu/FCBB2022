import sys

# Hard code codon table (Professor says must hard code)
Codon_Dict = {}
Codon_Dict.update(dict.fromkeys(['ATT','ATC','ATA'],'I'))
Codon_Dict.update(dict.fromkeys(['CTT','CTC','CTA','CTG','TTA','TTG'],'L'))
Codon_Dict.update(dict.fromkeys(['GTT','GTC','GTA','GTG'],'V'))
Codon_Dict.update(dict.fromkeys(['TTT','TTC'],'F'))
Codon_Dict.update(dict.fromkeys(['ATG'],'M'))
Codon_Dict.update(dict.fromkeys(['TGT','TGC'],'C'))
Codon_Dict.update(dict.fromkeys(['GCT','GCC','GCA','GCG'],'A'))
Codon_Dict.update(dict.fromkeys(['GGT','GGC','GGA','GGG'],'G'))
Codon_Dict.update(dict.fromkeys(['CCT','CCC','CCA','CCG'],'P'))
Codon_Dict.update(dict.fromkeys(['ACT','ACC','ACA','ACG'],'T'))
Codon_Dict.update(dict.fromkeys(['TCT','TCC','TCA','TCG','AGT','AGC'],'S'))
Codon_Dict.update(dict.fromkeys(['TAT','TAC'],'Y'))
Codon_Dict.update(dict.fromkeys(['TGG'],'W'))
Codon_Dict.update(dict.fromkeys(['CAA','CAG'],'Q'))
Codon_Dict.update(dict.fromkeys(['AAT','AAC'],'N'))
Codon_Dict.update(dict.fromkeys(['CAT','CAC'],'H'))
Codon_Dict.update(dict.fromkeys(['GAA','GAG'],'E'))
Codon_Dict.update(dict.fromkeys(['GAT','GAC'],'D'))
Codon_Dict.update(dict.fromkeys(['AAA','AAG'],'K'))
Codon_Dict.update(dict.fromkeys(['CGT','CGC','CGA','CGG','AGA','AGG'],'R'))
Codon_Dict.update(dict.fromkeys(['TAA','TAG','TGA'],'*'))

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
        translation_str += Codon_Dict[sequence_str[i:i+3]]
    return translation_str

# Translate and print each gene in Genes_Dict
for descriptor_str in Genes_Dict: 
    print(descriptor_str)
    print(translate_sequence(Genes_Dict[descriptor_str]))









