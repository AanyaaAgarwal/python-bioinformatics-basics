with open("sequence.fasta", "r") as file:
    for line in file:
        clean_line = line.rstrip("\n")
        
        if clean_line.startswith(">"):
            print("Header found:", clean_line)
        else:
            length = len(clean_line)
            G = clean_line.count("G")
            C = clean_line.count("C")
            gc_content = ((G + C) / length) * 100
            
            print("Sequence:", clean_line)
            print("Length:", length, "| GC Content:", gc_content, "%")
