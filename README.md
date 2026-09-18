# Python Bioinformatics Basics 🧬

A public collection of lightweight Python scripts and tools designed for biological sequence analysis, genomic data filtering, and sequence manipulation.

## 📌 Included Tools

- **`at_content_calculator.py`**: Calculates the percentage of Adenine and Thymine bases in a target DNA sequence.
- **`gc_content_calculator.py`**: Parses a list of DNA sequences, calculates GC content ratios, and filters for high-GC regions (>50%).
- **`read_dna_file.py`**: Processes external biological sequence files (`dna.txt`) line-by-line using safe File I/O (`with open`), calculates GC content, and strips formatting artifacts.
- **`fasta_parser.py`**: Parses structured FASTA format files (`sequence.fasta`), separating sequence header tags (`>`) from biological sequence data to calculate per-header GC metrics.
- **`reverse_complement.py`**: Converts a $5' \rightarrow 3'$ DNA sequence into its antiparallel $5' \rightarrow 3'$ reverse complement string.

## 📁 Sample Data

- **`dna.txt`**: Raw sequence input file for line-by-line parsing demonstrations.
- **`sequence.fasta`**: Structured FASTA file containing header metadata and DNA sequences.

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your machine.

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/AanyaaAgarwal/python-bioinformatics-basics.git
