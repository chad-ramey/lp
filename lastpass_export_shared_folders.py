"""
Script: LastPass Export Shared Folders

This script parses the output of the LastPass CLI command `lpass ls` to extract shared folder information.
It processes the folder names, file names, and unique IDs from the output and exports the data into a CSV file.

Usage:
- Place the LastPass `lpass ls` output in a text file (e.g., `lpass_ls.txt`).
- Run this script to generate a CSV file with columns: Folder Name, File Name, and ID.
- Use LastPass owner credentials

This script does not handle sensitive data (passwords, secrets, or credentials), making it safe to include in a public repository.
Ensure the input text file does not contain sensitive information.

Author: Chad Ramey
Date: January 16, 2025
"""

import csv

def parse_and_export_lpass_ls(input_file, output_csv):
    """Parse the lpass ls text output and export it to a formatted CSV."""
    try:
        # Read the input file
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Prepare data for CSV
        csv_data = []
        for line in lines:
            # Skip empty lines
            if line.strip():
                # Split by '[id:' to extract folder name and ID
                parts = line.rsplit("[id:", 1)
                if len(parts) == 2:
                    folder_and_file = parts[0].strip()
                    folder_id = parts[1].replace("]", "").strip()
                    
                    # Split folder and file by '/'
                    if "/" in folder_and_file:
                        folder_name, file_name = folder_and_file.split("/", 1)
                    else:
                        folder_name = folder_and_file
                        file_name = ""
                    
                    csv_data.append([folder_name, file_name, folder_id])

        # Write to the output CSV
        with open(output_csv, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Folder Name", "File Name", "ID"])
            writer.writerows(csv_data)

        print(f"CSV export completed successfully: {output_csv}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main script execution
if __name__ == "__main__":
    # Input file and output file paths
    input_file = "lpass_ls.txt"  # Replace with the path to your input text file
    output_csv = "shared_folders.csv"  # Replace with the desired output CSV file name

    # Execute the function
    parse_and_export_lpass_ls(input_file, output_csv)
