dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
text = dna.replace("A", "t")
text = text.replace("T", "a")
text = text.replace("C", "g")
text = text.replace("G", "c")

# Reversing string and making upper case
reverse_complement = text[::-1].upper()

print("Original DNA:", dna)
print("Reverse Complement:", reverse_complement)
