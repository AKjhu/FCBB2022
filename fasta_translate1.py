import sys

# Get descriptor_str and strip '\n'
descriptor_str = str.strip(sys.stdin.readline())

# Get sequence_str. Concatenate DNA lines and strip '\n'
sequence_str = ''
for line in sys.stdin: 
    sequence_str += str.strip(line)

# Initialize and print Fasta1_Dict
Fasta1_Dict = {descriptor_str: sequence_str}
for descriptor_str in Fasta1_Dict:
    sys.stdout.write(descriptor_str + ' : ' + Fasta1_Dict[descriptor_str] + '\n')
