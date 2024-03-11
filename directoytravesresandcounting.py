import os

def count_files_and_directories(directory):
    
    num_files = 0
    num_dirs = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                num_files += 1
            elif entry.is_dir():
                num_dirs += 1
        return num_files, num_dirs
    except PermissionError:
        print(f"Permission denied to access {directory}")
        return 0, 0
    except Exception as e:
        print(f"An error occurred while counting files and directories in {directory}: {e}")
        return 0, 0

def traverse_directory(start_dir, level=0, output_file=None):
    
    try:
        num_files, num_dirs = count_files_and_directories(start_dir)
        
        indent = '    ' * level
        output = f"{indent}Level {level}: Files - {num_files}, Directories - {num_dirs}\n"
        print(output)
        if output_file:
            output_file.write(output)

        if num_dirs > 0:
            for entry in os.scandir(start_dir):
                if entry.is_dir():
                    traverse_directory(entry.path, level + 1, output_file)
    except Exception as e:
        print(f"An error occurred while traversing {start_dir}: {e}")

if __name__ == "__main__":
    start_dir = input("Enter the starting directory path: ")

    
    with open('directory_stats.txt', 'w') as output_file:
        traverse_directory(start_dir, output_file=output_file)
