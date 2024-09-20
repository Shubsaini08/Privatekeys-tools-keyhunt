import os

def search_in_file(file_path, search_string):
    """Search for the exact string in a given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if search_string in line:
                    print(f"Match found in {file_path} on line {line_number}: {line.strip()}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def main():
    # List of files to search
    files_to_search = [
        'list.txt',
        'list2.txt',
        'list3.txt',
        'list4.txt',
        'list5.txt',
        'list6.txt',
        'list7.txt'
    ]
    
    # Prompt user for the string to search for
    search_string = input("Enter the exact string to search for: ").strip()
    
    # Ensure the search string is not empty
    if not search_string:
        print("You must enter a non-empty string to search for.")
        return

    # Search through each file
    for file_name in files_to_search:
        if os.path.isfile(file_name):
            search_in_file(file_name, search_string)
        else:
            print(f"{file_name} does not exist.")

if __name__ == "__main__":
    main()
