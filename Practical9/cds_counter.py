seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'  # DNA sequence
start_codon = 'ATG'  # Start codon
stop_codons = ['TAA', 'TAG', 'TGA']  # Stop codons

coding_sequences = 0  # Counter for coding sequences

# Loop through the DNA sequence and search for start and stop codons
for i in range(len(seq)):
    if seq[i:i+3] == start_codon:  # If start codon is found
        for stop_codon in stop_codons:
            if stop_codon in seq[i+3:]:  # If stop codon is found after start codon
                coding_sequences += 1

print("Total number of possible coding sequences:", coding_sequences)
