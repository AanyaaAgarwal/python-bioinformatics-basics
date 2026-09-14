# Calculate AT content of a DNA sequence
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_length = len(dna)

count_a = dna.count("A")
count_t = dna.count("T")

at_content = (count_a + count_t) / dna_length

print("The AT content is " + str(at_content))
