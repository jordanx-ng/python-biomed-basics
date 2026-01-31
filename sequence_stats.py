# sequence_stats.py
# Basic DNA sequence statistics calculator
# let me create a random sequence of DNA for demonstration

sequence = "ATGCGATACGCTTACGATCG" 
# each character reopresents a nucleotide: A, T, C, or G

length = len(sequence)
# counts how many characters are in the sequence, in this case its 20

count_A = sequence.count("A")
count_T = sequence.count("T")
count_C = sequence.count("C")
count_G = sequence.count("G")
#counts how many times each nucleotide appears in the sequence

print("Sequence length:", length)
print("A:", count_A)
print("T:", count_T)
print("C:", count_C)
print("G:", count_G)