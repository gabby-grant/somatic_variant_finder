# Somatic Mutation Finder
A Python utility tool for finding gene mutations in MAF (Mutation Annotation Format) files typically used in cancer genomics research. A somatic mutation is a genetic alteration that occurs in a body cell (somatic cell) after conception, but not in the germ cells (sperm or egg), and is therefore not inherited by offspring

## Description
`somatic_mutation_finder.py` is a tool designed to search through multiple directories for MAF files containing information about somatic mutations, and identify occurrences of a specific gene of interest. The script automates the process of:

1. Finding compressed MAF files in subdirectories
2. Copying them to a working directory
3. Decompressing them
4. Counting occurrences of the specified gene

This tool is particularly useful for researchers working with large cancer genomics datasets such as those from TCGA (The Cancer Genome Atlas) or other cancer sequencing projects.

## Installation
Clone this repository to your local machine:

```
git clone https://github.com/gabby-grant/somatic_variant_finder
cd somatic-mutation-finder
```

### Requirements
- Python 3.6 or higher
- Standard Python libraries (os, sys, gzip, shutil, glob)
- gdc-client version 1.6.1

## Usage
Run the script with a single argument - the gene name you want to search for:

``` python somatic_mutation_finder.py <gene_name> ```

### Parameters:
`<gene_name>` - The name of the gene you want to search for in the mutation files
## How It Works
1. The script searches all subdirectories in the current working directory for files with .maf or .mutation extensions
2. When it finds directories containing such files, it locates any compressed MAF files (.maf.gz) and copies them to the current directory
3. It then decompresses each .maf.gz file and searches for occurrences of the specified gene
4. Results are printed to the console, showing the count of gene occurrences in each file
   
## Example Output
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

- Chromosome
- Start position
- End position
- Reference allele
- Tumor allele
- Gene affected
- Mutation type
- Sample ID










 
