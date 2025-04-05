#!/usr/bin/env python3

import os
import sys
import gzip
import shutil
import glob
import argparse

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Find somatic mutations in compressed MAF files.')
    parser.add_argument('-p', '--path', default='.', 
                        help='Base path to search for mutation files (default: current directory)')
    parser.add_argument('-o', '--output_dir', default='.',
                        help='Directory where to save output files (default: current directory)')
    args = parser.parse_args()
    
    base_path = args.path
    output_dir = args.output_dir
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read gene names from genes.list file
    gene_file = os.path.join(output_dir, "genes.list")
    if not os.path.isfile(gene_file):
        print(f"Error: {gene_file} not found")
        sys.exit(1)
        
    with open(gene_file, 'r') as f:
        genes = [line.strip() for line in f if line.strip()]
    
    print(f"Loaded {len(genes)} genes from {gene_file}")
    
    # Dictionary to track matches for each gene
    gene_matches = {gene: 0 for gene in genes}
    
    # Step 1: Find directories with mutation files and copy compressed files up
    print(f"Searching for mutation files in: {base_path}")
    for dir_path, dir_names, file_names in os.walk(base_path):
        # Skip the output directory if it's under the base path
        if os.path.abspath(dir_path) == os.path.abspath(output_dir):
            continue
            
        # Look for mutation files in this directory
        mutation_files = glob.glob(f"{dir_path}/*.maf") + glob.glob(f"{dir_path}/*.mutation")
        compressed_files = glob.glob(f"{dir_path}/*.maf.gz")
        
        if mutation_files or compressed_files:
            print(f"Found mutation data in directory: {dir_path}")
            
            # Copy compressed files to output directory
            for file in compressed_files:
                destination = os.path.join(output_dir, os.path.basename(file))
                shutil.copy(file, destination)
                print(f"Copied {file} to {destination}")
    
    # Step 2: Process each compressed maf file in the output directory
    print("\nProcessing compressed files...")
    for maf_file in glob.glob(os.path.join(output_dir, "*.maf.gz")):
        print(f"Processing file: {maf_file}")
        
        # Uncompress the file
        output_file = maf_file[:-3]  # Remove .gz extension
        with gzip.open(maf_file, 'rt') as f_in:
            with open(output_file, 'w') as f_out:
                content = f_in.read()
                f_out.write(content)
        
        # Count matches for each gene
        with open(output_file, 'r') as f:
            for line in f:
                for gene in genes:
                    if gene in line:
                        gene_matches[gene] += 1
        
        # Print summary for this file
        file_matches = sum(gene_matches.values())
        print(f"Found total of {file_matches} gene matches in {output_file}")
        print("------------------------------------")
    
    # Step 3: Output results to files
    
    # (6) Output the number of matches to a text file
    match_counts_file = os.path.join(output_dir, "match_counts.txt")
    total_matches = sum(gene_matches.values())
    with open(match_counts_file, 'w') as f:
        f.write(f"Total matches across all files: {total_matches}\n\n")
        f.write("Gene\tMatches\n")
        for gene, count in gene_matches.items():
            f.write(f"{gene}\t{count}\n")
    
    # (7) Output genes not found in any file
    not_found_file = os.path.join(output_dir, "genes_not_found.txt")
    not_found_genes = [gene for gene, count in gene_matches.items() if count == 0]
    with open(not_found_file, 'w') as f:
        for gene in not_found_genes:
            f.write(f"{gene}\n")
    
    print(f"\nResults summary:")
    print(f"- Total matches: {total_matches}")
    print(f"- Genes found: {len(genes) - len(not_found_genes)}")
    print(f"- Genes not found: {len(not_found_genes)}")
    print(f"- Match counts written to: {match_counts_file}")
    print(f"- Genes not found written to: {not_found_file}")

if __name__ == "__main__":
    main()
    
