input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  # Input FASTA file
output_file = 'TGA_genes.fa'  # Output FASTA file

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    gene_name = ''  # Variable to store gene name
    sequence = ''  # Variable to store sequence
    for line in infile:
        if line.startswith('>'):  # If line starts with '>'
            if sequence.endswith('TGA'):  # If previous sequence ends with 'TGA'
                # Write gene name and sequence to output file
                outfile.write(f'>{gene_name}\n{sequence}\n')
            gene_name = line.strip().split()[0][1:]  # Extract gene name from header
            sequence = ''  # Reset sequence variable
        else:
            sequence += line.strip()  # Concatenate sequence lines

    if sequence.endswith('TGA'):  # Check last sequence after loop
        # Write gene name and sequence to output file
        outfile.write(f'>{gene_name}\n{sequence}\n')





