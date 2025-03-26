#!/usr/bin/env python3

import os
import sys
import gzip
import shutil
import glob

def main():
    # Check if gene name is provided
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <gene_name>")
        sys.exit(1)
        
    gene_name = sys.argv[1]
    print(f"Searching for gene: {gene_name}")
    
    # Step 1: Find directories with mutation files and copy compressed files up
    print("Copying compressed files from subdirectories...")
    for dir_name in [d for d in os.listdir() if os.path.isdir(d)]:
        mutation_files = glob.glob(f"{dir_name}/*.maf") + glob.glob(f"{dir_name}/*.mutation")
        
        if mutation_files:
            print(f"Found mutation data in directory: {dir_name}")
            
            # Find compressed maf files and copy them up one level
            compressed_files = glob.glob(f"{dir_name}/*.maf.gz")
            for file in compressed_files:
                shutil.copy(file, ".")
                print(f"Copied {file} to current directory")
    
    # Step 2: Process each compressed maf file
    print("\nProcessing compressed files...")
    for maf_file in glob.glob("*.maf.gz"):
        print(f"Processing file: {maf_file}")
        
        # Uncompress the file
        output_file = maf_file[:-3]  # Remove .gz extension
        with gzip.open(maf_file, 'rt') as f_in:
            with open(output_file, 'w') as f_out:
                content = f_in.read()
                f_out.write(content)
        
        # Count matches
        match_count = 0
        with open(output_file, 'r') as f:
            for line in f:
                if gene_name in line:
                    match_count += 1
        
        print(f"Found {match_count} occurrences of {gene_name} in {output_file}")
        print("------------------------------------")

if __name__ == "__main__":
    main()