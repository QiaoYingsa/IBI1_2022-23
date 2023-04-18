def dna_coding_status(dna_sequence):
    """
    Determines the coding status of a given DNA sequence.

    Args:
        dna_sequence (str): DNA sequence to be analyzed.

    Returns:
        tuple: A tuple containing the coding status ('protein-coding', 'non-coding', or 'unclear')
               and the percentage of the sequence that is coding (float).
    """
    # Convert DNA sequence to uppercase for consistency
    dna_sequence = dna_sequence.upper()

    # Find the indices of the start and stop codons in the DNA sequence
    start_codon_index = dna_sequence.find('ATG')
    stop_codon_index = dna_sequence.find('TGA')

    # If either start or stop codon is not found, return 'unclear' status
    if start_codon_index == -1 or stop_codon_index == -1:
        return 'unclear', 0.0

    # Calculate the length of the DNA sequence
    seq_length = len(dna_sequence)

    # Calculate the percentage of the sequence that is coding
    coding_length = stop_codon_index - start_codon_index + 3
    coding_percentage = (coding_length / seq_length) * 100

    # Determine the coding status based on the coding percentage
    if coding_percentage > 50:
        return 'protein-coding', coding_percentage
    elif coding_percentage < 10:
        return 'non-coding', coding_percentage
    else:
        return 'unclear', coding_percentage


# Example usage:
dna_seq1 = 'ATGAGCGTAGCTGA'
dna_seq2 = 'TTTAGCGTAGCTGA'
dna_seq3 = 'ATGCGTAGCTGA'
coding_status1, coding_percentage1 = dna_coding_status(dna_seq1)
coding_status2, coding_percentage2 = dna_coding_status(dna_seq2)
coding_status3, coding_percentage3 = dna_coding_status(dna_seq3)
print("DNA Sequence 1: Coding Status - {}, Coding Percentage - {:.2f}%".format(coding_status1, coding_percentage1))
print("DNA Sequence 2: Coding Status - {}, Coding Percentage - {:.2f}%".format(coding_status2, coding_percentage2))
print("DNA Sequence 3: Coding Status - {}, Coding Percentage - {:.2f}%".format(coding_status3, coding_percentage3))
