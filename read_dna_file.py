with open("dna.txt", "r") as file:
    for line in file:
        clean_line = line.rstrip("\n")
        length = len(clean_line)
        G = clean_line.count("G")
        C = clean_line.count("C")
        gc_content = ((G + C) / length) * 100
        print("The GC content percentage for sequence", clean_line, "is:", gc_content, "%")
