sequences = ["ATGCGCTA", "AATTATAA", "GCGCGCAT", "ATATATAT", "GCCCGCGA"]

for seq in sequences: 
    G = seq.count("G")
    C = seq.count("C")
    length = len(seq)
    GC_content = ((G + C) / length) * 100
    
    if GC_content > 50:
        print("Sequence", seq, "has a GC content greater than 50%, that is:", GC_content, "%")
