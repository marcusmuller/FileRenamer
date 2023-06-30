import os
import time

def rename_files(folder_path, include_subfolders, input_format, output_format):
    count = 0

    start_time = time.time()

    for root, dirs, files in os.walk(folder_path):
        if not include_subfolders and root != folder_path:
            break
        for file in files:
            if file.lower().endswith(input_format):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file[:file.rfind(".")] + output_format)
                os.rename(old_file_path, new_file_path)
                count += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    return count, elapsed_time

# Example usage
folder_path = "path/to/folder"
include_subfolders = True
input_format = ".ts"
output_format = ".mp4"

count, elapsed_time = rename_files(folder_path, include_subfolders, input_format, output_format)
print(f"File renaming completed!\nTotal files renamed: {count}\nElapsed time: {elapsed_time:.2f} seconds")
