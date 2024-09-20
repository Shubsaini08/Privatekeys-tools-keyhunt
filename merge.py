import heapq

def merge_text_files(file_paths, output_file):
    with open(output_file, 'w') as merged_file:
        heap = []
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                for line in file:
                    heapq.heappush(heap, line.strip())
                    if len(heap) > 100_000_000:  # Limiting the heap size
                        merged_file.write(heapq.heappop(heap) + '\n')

        while heap:
            merged_file.write(heapq.heappop(heap) + '\n')

if __name__ == "__main__":
    file_paths = ["hdwif.txt", "keys.txt", "brute2.txt", "brute3.txt"]  # Add your file paths here
    merge_text_files(file_paths, 'LIsT.txt')
