stop_codon = input("Enter the stop codon (TAA, TAG, or TGA): ")
output_file = f'{stop_codon}_stop_genes.fa'  # Output FASTA file

# Open input and output files
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, open(output_file, 'w') as outfile:
    gene_name = ''  # Variable to store gene name
    sequence = ''  # Variable to store sequence
    count = 1  # Variable to store count of coding sequences
    for line in infile:
        if line.startswith('>'):  # If line starts with '>'
            if sequence.endswith(stop_codon):  # If previous sequence ends with the given stop codon
                # Write gene name and sequence to output file
                outfile.write(f'>{gene_name} ({count} coding sequences)\n{sequence}\n')
                count += 1  # Increment count of coding sequences
            gene_name = line.strip().split()[0][1:]  # Extract gene name from header
            sequence = ''  # Reset sequence variable
        else:
            sequence += line.strip()  # Concatenate sequence lines

    if sequence.endswith(stop_codon):  # Check last sequence after loop
        # Write gene name and sequence to output file
        outfile.write(f'>{gene_name} ({count} coding sequences)\n{sequence}\n')

print(f'Sequences of genes ending with {stop_codon} written to {output_file}.')
