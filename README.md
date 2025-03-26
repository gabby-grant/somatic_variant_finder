# Somatic Mutation Finder
A Python utility tool for finding gene mutations in MAF (Mutation Annotation Format) files typically used in cancer genomics research.

## Description
somatic_mutation_finder.py is a tool designed to search through multiple directories for MAF files containing information about somatic mutations, and identify occurrences of a specific gene of interest. The script automates the process of:

Finding compressed MAF files in subdirectories
Copying them to a working directory
Decompressing them
Counting occurrences of the specified gene
This tool is particularly useful for researchers working with large cancer genomics datasets such as those from TCGA (The Cancer Genome Atlas) or other cancer sequencing projects.

## Installation
Clone this repository to your local machine:

git clone https://github.com/yourusername/somatic-mutation-finder.git
cd somatic-mutation-finder
Requirements
Python 3.6 or higher
Standard Python libraries (os, sys, gzip, shutil, glob)
No additional package installation is required as the script uses only Python built-in libraries.

## Usage
Run the script with a single argument - the gene name you want to search for:

``` python somatic_mutation_finder.py <gene_name> ```

For example:

``` python somatic_mutation_finder.py TP53 ```

Parameters
`<gene_name>`: The name of the gene you want to search for in the mutation files
## How It Works
The script searches all subdirectories in the current working directory for files with .maf or .mutation extensions
When it finds directories containing such files, it locates any compressed MAF files (.maf.gz) and copies them to the current directory
It then decompresses each .maf.gz file and searches for occurrences of the specified gene
Results are printed to the console, showing the count of gene occurrences in each file
Example Output
```
Searching for gene: TP53
Copying compressed files from subdirectories...
Found mutation data in directory: TCGA-BRCA
Copied TCGA-BRCA/sample1.maf.gz to current directory
Copied TCGA-BRCA/sample2.maf.gz to current directory

Processing compressed files...
Processing file: sample1.maf.gz
Found 15 occurrences of TP53 in sample1.maf
------------------------------------
Processing file: sample2.maf.gz
Found 8 occurrences of TP53 in sample2.maf
------------------------------------
```

## Data Format
This script works with MAF (Mutation Annotation Format) files, which are tab-delimited files that contain somatic mutation information from cancer sequencing projects. MAF files typically include information such as:

Chromosome
Start position
End position
Reference allele
Tumor allele
Gene affected
Mutation type
Sample ID
And many other annotations
Future Enhancements
Potential future improvements for this tool:

Output results to a CSV or TSV file
Include more detailed information about the mutations found
Add filtering options for mutation types
Implement parallel processing for large datasets
Add visualization options for results
## License
This project is licensed under the  License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.








 
