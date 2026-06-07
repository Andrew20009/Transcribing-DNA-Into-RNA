# Transcribing DNA into RNA

## OVERVIEW
This program reads a DNA sequence from a text file and changes the sequence to **RNA**; changes <u>T in the DNA sequence to U in the RNA sequence</u>.
It is a solution to the **"Transcribing DNA into RNA"** Rosalind problem **(ID: RNA)**. The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

---

## FEATURES
- Reads DNA sequence from a file <u>(rosalind_rna.txt)</u>
- Automatically converts input to **uppercase**
- Creates <u>RNA sequence (rna)</u>
- Converts **T** nucleotide in the DNA into **U** nucleotide in the RNA sequence
- Leaves <u>A, C, G</u> untouched
- Fast and memory-efficient — works well with long sequences
- Clean, well-commented code with proper functions and docstrings

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the Input txt with name rosalind_rna.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_rna.txt):
```
TCCGTAAGACTAGC
```
**Output:**
```
UCCGUAAGACUAGC
```

---

## HOW IT WORKS
1. The program reads the DNA sequence from the file
2. It cleans the input (removes whitespace and converts to **uppercase**)
3. It changes all <u>T letters to U</u> and puts everything in the **(rna)** sequence
4. Finally, it prints the **RNA sequence**

---

## TECHNOLOGIES USED
- **Python**
- **File I/O** (txt)
