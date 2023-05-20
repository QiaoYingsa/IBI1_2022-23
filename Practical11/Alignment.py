def compare_sequences(seq1, seq2):
    # Define the BLOSUM62 matrix
    blosum62 = {
        ('A', 'A'): 4, ('R', 'R'): 5, ('N', 'N'): 6, ('D', 'D'): 6, ('C', 'C'): 9, ('Q', 'Q'): 5, ('E', 'E'): 5,
        ('G', 'G'): 6, ('H', 'H'): 8, ('I', 'I'): 4, ('L', 'L'): 4, ('K', 'K'): 5, ('M', 'M'): 5, ('F', 'F'): 6,
        ('P', 'P'): 7, ('S', 'S'): 4, ('T', 'T'): 5, ('W', 'W'): 11, ('Y', 'Y'): 7, ('V', 'V'): 4, ('B', 'B'): 5,
        ('Z', 'Z'): 5, ('X', 'X'): -1, ('*', '*'): -4
    }

    score = 0
    identical_count = 0
    total_count = 0

    # Compare each amino acid in the sequences
    for aa1, aa2 in zip(seq1, seq2):
        total_count += 1
        if (aa1, aa2) in blosum62:
            score += blosum62[(aa1, aa2)]
            if aa1 == aa2:
                identical_count += 1
        elif (aa2, aa1) in blosum62:  # Check reverse pair
            score += blosum62[(aa2, aa1)]
            if aa1 == aa2:
                identical_count += 1
        else:
            score += blosum62[('X', 'X')]  # Use a default score for unknown pairs

    percentage_identical = (identical_count / total_count) * 100 if total_count > 0 else 0

    return score, percentage_identical


def run_pairwise_combinations():
    sequences = {
        'human': 'ACE2_human.fa',
        'mouse': 'ACE2_mouse.fa',
        'cat': 'ACE2_cat.fa'
    }

    combinations = [('human', 'mouse'), ('human', 'cat'), ('mouse', 'cat')]

    for combination in combinations:
        sequence1 = combination[0]
        sequence2 = combination[1]

        with open(sequences[sequence1], 'r') as file1, open(sequences[sequence2], 'r') as file2:
            seq1 = file1.read()
            seq2 = file2.read()

            # Find the starting index for each sequence
            if sequence1 == 'human':
                start_index1 = seq1.index("> ACE2_HUMAN (Q9BYF1)") + len("> ACE2_HUMAN (Q9BYF1)")
                seq1 = seq1[start_index1:].strip()
            elif sequence1 == 'mouse':
                start_index1 = seq1.index(">ACE2_MOUSE (Q8R0I0) ") + len(">ACE2_MOUSE (Q8R0I0)")
                seq1 = seq1[start_index1:].strip()
            elif sequence1 == 'cat':
                start_index1 = seq1.index("> ACE2_CAT (Q56H28)") + len("> ACE2_CAT (Q56H28)")
                seq1 = seq1[start_index1:].strip()

            if sequence2 == 'human':
                start_index2 = seq2.index("> ACE2_HUMAN (Q9BYF1)") + len("> ACE2_HUMAN (Q9BYF1)")
                seq2 = seq2[start_index2:].strip()
            elif sequence2 == 'mouse':
                start_index2 = seq2.index(">ACE2_MOUSE (Q8R0I0)") + len(">ACE2_MOUSE (Q8R0I0)")
                seq2 = seq2[start_index2:].strip()
            elif sequence2 == 'cat':
                start_index2 = seq2.index("> ACE2_CAT (Q56H28)") + len("> ACE2_CAT (Q56H28)")
                seq2 = seq2[start_index2:].strip()

            score, percentage_identical = compare_sequences(seq1, seq2)
            print_alignment_score(sequence1, sequence2, score, percentage_identical)


def print_alignment_score(sequence1, sequence2, score, percentage_identical):
    print(f"Alignment score for {sequence1} and {sequence2}: {score}")
    print(f"Percentage of identical amino acids: {percentage_identical:.2f}%\n")


run_pairwise_combinations()

