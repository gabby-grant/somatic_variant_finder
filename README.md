# Somatic Mutation Finder

A Python utility for finding somatic mutations in compressed MAF (Mutation Annotation Format) files across specified directories.

## Overview

This tool recursively searches for `.maf.gz` files in a given directory, processes them to find specified genes from a `genes.list` file, and reports the number of matches for each gene across all files.

## Features

- Recursive search for mutation files through directory structures
- Support for compressed (`.maf.gz`) files
- Customizable input and output paths
- Gene match counting across multiple files
- Summary reporting for genes found and not found

## Requirements

- Python 3.6+
- Standard Python libraries (no external dependencies)

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/somatic-mutation-finder.git
cd somatic-mutation-finder
```

Make the script executable:

```bash
chmod +x somatic_mutation_finder.py
```

## Usage

### Basic Usage

```bash
python3 somatic_mutation_finder.py
```

This will search for mutation files in the current directory and use the current directory for output.

### Command Line Arguments

```
usage: somatic_mutation_finder.py [-h] [-p PATH] [-o OUTPUT_DIR]

Find somatic mutations in compressed MAF files.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Base path to search for mutation files (default: current directory)
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Directory where to save output files (default: current directory)
```

### Examples

Search for mutation files in a specific directory:
```bash
python3 somatic_mutation_finder.py --path /path/to/mutation/files
```

Specify both search path and output directory:
```bash
python3 somatic_mutation_finder.py --path /path/to/mutation/files --output_dir /path/for/results
```

## Input Files

### genes.list

Create a file named `genes.list` in your output directory with each gene name on a separate line:

```
TP53
BRCA1
BRCA2
...
```

## Output Files

The script generates two main output files:

### match_counts.txt

Contains the number of matches for each gene across all processed files:

```
Total matches across all files: 352

Gene    Matches
TP53    125
BRCA1   98
BRCA2   87
...
```

### genes_not_found.txt

Lists genes from `genes.list` that weren't found in any of the processed files:

```
GENE4
GENE7
...
```

## Process Flow

1. Reads gene names from `genes.list`
2. Recursively searches for `.maf.gz` files in the specified directory
3. Copies and uncompresses the files to the output directory
4. Processes each file to count gene matches
5. Outputs summary statistics and detailed results

## Data Format
This script works with MAF (Mutation Annotation Format) files, which are tab-delimited files that contain somatic mutation information from cancer sequencing projects. MAF files typically include information such as:

- Chromosome
- Start position
- End position
- Reference allele
- Tumor allele
- Gene affected
- Mutation type
- Sample ID










 
