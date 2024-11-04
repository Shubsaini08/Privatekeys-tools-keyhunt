import heapq
import re

# Pattern to match Bitcoin addresses
BITCOIN_ADDRESS_PATTERN = r'\b(1[0-9A-Za-z]{25,34}|3[0-9A-Za-z]{25,34}|bc1[0-9A-Za-z]{25,200})\b'

def merge_and_extract_addresses(file_paths, output_file, heap_limit=100_000):
    """
    Merges multiple files by extracting Bitcoin addresses and writing them to a single output file.
    
    Args:
        file_paths (list): List of file paths to merge.
        output_file (str): Output file path for merged and extracted Bitcoin addresses.
        heap_limit (int): Maximum number of items to hold in the heap to limit memory usage.
    """
    heap = []
    pattern = re.compile(BITCOIN_ADDRESS_PATTERN)
    
    with open(output_file, 'w') as merged_file:
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                for line in file:
                    # Extract Bitcoin addresses from the line
                    bitcoin_addresses = pattern.findall(line)
                    # Add each address to the heap
                    for address in bitcoin_addresses:
                        heapq.heappush(heap, address)
                    
                    # If heap size exceeds limit, flush smallest items to file
                    while len(heap) > heap_limit:
                        merged_file.write(heapq.heappop(heap) + '\n')
        
        # Write remaining items in the heap to the file
        while heap:
            merged_file.write(heapq.heappop(heap) + '\n')

if __name__ == "__main__":
    # Specify file paths to merge
    file_paths = ["balance01.txt", "balance02.txt", "balance03.txt", "balance04.txt", "balance05.txt", "balance06.txt", "balance07.txt", "balance08.txt", "balance09.txt", "balance10.txt", "balance11.txt", "balance12.txt", "btc_000002.txt", "btc_000003.txt", "btc_000004.txt", "btc_000001.txt", "btc_000005.txt", "btc_000006.txt", "btc_balance.txt", "btc_balance2.txt", "btc_balance3.txt", "puzzaddmain.txt", "puzzadd.txt"]  # Add your file paths here
    output_file = 'btc_merged_extracted.txt'
    merge_and_extract_addresses(file_paths, output_file)
