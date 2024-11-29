import os

def find_files_with_string(directory, search_string, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as out_file:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):  # Check if the file is a text file
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as in_file:
                        file_contains_string = False
                        for line in in_file:
                            if search_string in line:  # Check if the line contains the search string
                                file_contains_string = True
                                break
                        if file_contains_string:
                            out_file.write(file_path + '\n')  # Write the file path to the output file

if __name__ == "__main__":
    # Get the search string from the user
    search_string = input("Please enter the string to search for (e.g., Bitcoin address): ")
    # Define the directory to scan and the output file name
    directory_to_scan = "scanned_pages"
    output_file = "MONEY.txt"
    
    # Call the function to find and log files containing the search string
    find_files_with_string(directory_to_scan, search_string, output_file)
    
    print(f"Finished scanning. Any files containing the search string have been listed in {output_file}.")

