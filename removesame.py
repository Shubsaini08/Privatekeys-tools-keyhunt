import re

# Define the pattern for Bitcoin addresses
pattern = r'\b(1[0-9A-Za-z]{25,34}|3[0-9A-Za-z]{25,34}|bc1[0-9A-Za-z]{25,100})\b'

def extract_addresses(file_path):
    """Extract Bitcoin addresses from a given file."""
    addresses = set()
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            addresses.update(matches)
    return addresses

def check_addresses(bitcoin_addresses, log_file_path):
    """Check which Bitcoin addresses are present in the log file."""
    matched_addresses = set()
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            matched_addresses.update(re.findall(pattern, line))
    return matched_addresses

def write_unmatched_addresses(bitcoin_addresses, matched_addresses, output_file_path):
    """Write unmatched Bitcoin addresses to the output file."""
    unmatched_addresses = bitcoin_addresses - matched_addresses
    with open(output_file_path, 'w') as output_file:
        for address in unmatched_addresses:
            output_file.write(f"{address}\n")

def main():
    # File paths
    bit_file_path = 'bit.txt'
    log_file_path = 'check.log'
    output_file_path = 'BIT.txt'

    # Extract Bitcoin addresses from bit.txt
    bitcoin_addresses = extract_addresses(bit_file_path)

    # Check addresses against check.log
    matched_addresses = check_addresses(bitcoin_addresses, log_file_path)

    # Write unmatched addresses to BIT.txt
    write_unmatched_addresses(bitcoin_addresses, matched_addresses, output_file_path)

    print(f"Unmatched Bitcoin addresses have been written to {output_file_path}")

if __name__ == "__main__":
    main()
