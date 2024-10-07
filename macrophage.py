import os
import shutil
import re

def delete_folders_with_regex(root_folder, regex_pattern):
    pattern = re.compile(regex_pattern)
    for dirpath, dirnames, _ in os.walk(root_folder):
        for dirname in dirnames:
            if pattern.match(dirname):
                full_path = os.path.join(dirpath, dirname)
                print(f'Found {dirname} in {dirpath}')
                choice = input('Do you want to delete it? (y/n): ').strip().lower()
                if choice in ['y', '']:
                    shutil.rmtree(full_path)
                    print(f'Deleted {dirname} in {dirpath}')

if __name__ == "__main__":
    print("This script will search for folders matching a regex pattern and prompt you to delete them.")
    regex_pattern = input('Enter the regex pattern to match folder names (e.g., "node_modules"): ')
    root_folder = os.getcwd()
    delete_folders_with_regex(root_folder, regex_pattern)
