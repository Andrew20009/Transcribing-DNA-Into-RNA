def read_dna_from_txt(file_path: str) -> str: 
    # Function that reads nucleotide sequence from txt file
    sequence = "" # Initialize empty variable for the sequence
    
    with open(file_path) as f: # Open the file for reading
        for line in f: 
            cleaned = line.strip().upper() # Remove whitespace and convert to uppercase
            sequence += cleaned 
    
    return sequence 


def change_nucleotides(sequence: str) -> str:
    #Function that transcribes DNA into RNA; changes T to U.
    rna = ""                    # Creates empty variable for RNA
    
    for nucleotide in sequence:
        if nucleotide == 'T': # Checks if nucleoptide is T
            rna += 'U'          # Changes nucleotide T to U in the sequence
        else:
            rna += nucleotide   # A, C, G remain intouched
    
    return rna 


if __name__ == "__main__": # Main branch of the code
    file = "rosalind_rna.txt" #Gives name of varible (rosalind_rna.txt)
    
    seq = read_dna_from_txt(file) 
    rna = change_nucleotides(seq)
    
    print(rna)   # Prints RNA sequence