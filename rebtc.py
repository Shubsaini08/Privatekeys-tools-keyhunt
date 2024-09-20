import re

# Function to extract Bitcoin addresses from a string
def extract_bitcoin_addresses(text):
    pattern = r'\b(1[0-9A-Za-z]{25,34}|3[0-9A-Za-z]{25,34}|bc1[0-9A-Za-z]{25,39})\b'
    bitcoin_addresses = re.findall(pattern, text)
    return bitcoin_addresses

# Open the input and output files
with open('key.txt', 'r') as infile, open('B.txt', 'w') as outfile:
    for line in infile:
        # Extract Bitcoin addresses from the current line
        bitcoin_addresses = extract_bitcoin_addresses(line)
        # Write each extracted address to the output file
        for address in bitcoin_addresses:
            outfile.write(address + '\n')

