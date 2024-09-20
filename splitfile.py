def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for line in f)

def split_large_file(input_file, block_file, list_addresses_file):
    total_lines = count_lines(input_file)
    half_lines = total_lines // 2
    
    with open(input_file, 'r') as infile, \
         open(block_file, 'w') as block_outfile, \
         open(list_addresses_file, 'w') as list_addresses_outfile:
        
        for current_line, line in enumerate(infile):
            if current_line < half_lines:
                block_outfile.write(line)
            else:
                list_addresses_outfile.write(line)

if __name__ == "__main__":
    # Define your file paths here
    input_file_path = 'outputs.txt'
    block_file_path = 'out1.txt'
    list_addresses_file_path = 'out2.txt'
    
    split_large_file(input_file_path, block_file_path, list_addresses_file_path)


