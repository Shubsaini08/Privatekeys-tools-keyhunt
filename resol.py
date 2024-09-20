import re
import os

# Regular expression pattern to match Solana addresses
solana_address_pattern = r'\b[1-9A-HJ-NP-Za-km-z]{44}\b'

# Input and output file names
input_file = 'sollist.txt'
output_file = 'sol.txt'

# Function to process a chunk of data
def process_chunk(chunk):
    addresses = re.findall(solana_address_pattern, chunk)
    return '\n'.join(addresses)

# Function to read and process the input file
def process_file():
    chunk_size = 1024 * 1024  # 1 MB chunk size
    total_size = os.path.getsize(input_file)

    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            valid_addresses = process_chunk(chunk)
            out.write(valid_addresses)
            out.write('\n')  # Add a newline after each chunk

            print(f"Processed {f.tell()}/{total_size} bytes ({f.tell() * 100 / total_size:.2f}%)")

    print(f"Processing complete. Output written to {output_file}")

# Run the script
process_file()
