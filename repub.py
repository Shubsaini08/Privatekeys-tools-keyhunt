def filter_public_keys(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Open output file for writing
    with open(output_file, 'w') as outfile:
        for line in lines:
            # Strip whitespace and split by spaces
            keys = line.strip().split()
            for key in keys:
                # Check if the key starts with '02' or '03'
                if key.startswith('02') or key.startswith('03'):
                    outfile.write(key + '\n')

if __name__ == "__main__":
    filter_public_keys('public.txt', 'pub.txt')

