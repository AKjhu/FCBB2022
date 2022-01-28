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

# Read in and concatenate DNA information
descriptor_str = str.strip(sys.stdin.readline())
sequence_str = ''
for line in sys.stdin:
    sequence_str += str.strip(line)

# Translate sequence_str into amino acids
translation_str = ''
sequence_len = len(sequence_str)
for i in range(0, sequence_len, 3):
    #Stay within sesquence bounds
    if ((i + 3) > sequence_len):
        break
    translation_str += Codon_Dict[sequence_str[i:i+3]]

# Print translation in FASTA form
sys.stdout.write(descriptor_str + '\n' + translation_str + '\n')
