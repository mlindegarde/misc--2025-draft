#!/usr/bin/env python3
"""
Script to clean the 2025-available-players.csv file by splitting the team abbreviation 
from the Player column and creating a new Team column.
"""

import csv
import re
import sys
import os

def clean_player_data(input_file, output_file=None):
    """
    Clean the CSV data by splitting Player column into Player and Team columns.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file (defaults to input_file if None)
    """
    if output_file is None:
        output_file = input_file
    
    # Read and process the data
    cleaned_data = []
    
    with open(input_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Extract team from player name using regex
            player_text = row['Player']
            match = re.search(r'(.+?)\s*\(([^)]+)\)\s*$', player_text)
            
            if match:
                player_name = match.group(1).strip()
                team_abbr = match.group(2).strip()
            else:
                # If no team found, use the whole string as player name
                player_name = player_text.strip()
                team_abbr = ''
            
            # Create new row with cleaned data
            cleaned_row = {
                'Rank': row['Rank'],
                'Player': player_name,
                'Team': team_abbr,
                'Position': row['Position'],
                'Age': row['Age'],
                'Best Draft Position': row['Best Draft Position'],
                'Worst Draft Position': row['Worst Draft Position'],
                'Average Draft Position': row['Average Draft Position'],
                'Draft Position Standard Deviation': row['Draft Position Standard Deviation']
            }
            cleaned_data.append(cleaned_row)
    
    # Write the cleaned data
    fieldnames = [
        'Rank', 'Player', 'Team', 'Position', 'Age', 
        'Best Draft Position', 'Worst Draft Position', 
        'Average Draft Position', 'Draft Position Standard Deviation'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)
    
    print(f"Cleaned data written to {output_file}")
    print(f"Processed {len(cleaned_data)} rows")

def main():
    # Path to the CSV file
    csv_file = '/home/runner/work/misc--2025-draft/misc--2025-draft/veteran-draft/2025-available-players.csv'
    
    if not os.path.exists(csv_file):
        print(f"Error: File {csv_file} not found")
        sys.exit(1)
    
    print(f"Processing {csv_file}...")
    clean_player_data(csv_file)
    print("CSV cleaning completed!")

if __name__ == '__main__':
    main()