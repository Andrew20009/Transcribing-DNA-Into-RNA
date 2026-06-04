def read_dna_from_txt(file_path: str) -> str:
    # Reads nucleotide sequence from a txt file
    sequence = "" # Initialize empty variable for the sequence

    with open(file_path) as f: # Open the file for reading
        for line in f:
            cleaned = line.strip().upper() # Remove whitespace and convert to uppercase
            sequence += cleaned

    return sequence


def change_nucleotides(sequence: str) -> str:
    # Transcribes DNA into RNA by replacing T with U
    rna = "" # Creates empty variable for RNA

    for nucleotide in sequence:
        if nucleotide == 'T': # Checks if nucleotide is T
            rna += 'U' # Changes nucleotide T to U in the sequence
        else:
            rna += nucleotide # A, C, G remain untouched

    return rna


if __name__ == "__main__": # Entry point of the code
    file = "rosalind_rna.txt" # Path to the input file

    seq = read_dna_from_txt(file)
    rna = change_nucleotides(seq)

    print(rna) # Prints RNA sequence
