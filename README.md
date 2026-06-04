Transcribing DNA into RNA

OVERVIEW

This program reads a DNA sequence from a text file and changes the sequence to RNA; it changes T in the DNA sequence to U in the RNA sequence.
It is a solution to the "Transcribing DNA into RNA" Rosalind problem (ID: RNA). The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

FEATURES

Reads DNA sequence from a file (rosalind_rna.txt)
Automatically converts input to uppercase
Creates RNA sequence (rna)
Converts the T nucleotide in the DNA into the U nucleotide in the RNA sequence.
Leaves A, C, and G untouched.
Fast and memory-efficient — works well with long sequences
Clean, well-commented code with proper functions and docstrings


EXAMPLE
Input (rosalind_rna.txt): TCCGTAAGACTAGC
Output: UCCGUAAGACUAGC

HOW IT WORKS

The program reads the DNA sequence from the file.
It cleans the input (removes whitespace and converts to uppercase).
It changes all T letters in the file to U and puts everything in the (rna) sequence.
Finally, it prints the RNA sequence.


TECHNOLOGIES USED

Python
File txt
