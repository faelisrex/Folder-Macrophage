# Folder Cleanup Script

This script recursively searches for folders matching a given regex pattern from the directory where the script is run. It then prompts the user to decide whether to delete the matching folders.

## Features

- Recursively searches through all folders within the starting directory.
- Finds folders with names that match a specified regex pattern (e.g., `node_modules`).
- Prompts the user with the option to delete each matching folder.
- Deletes the folder if the user confirms with `y`, `Y`, or simply presses enter.

## Requirements

- Python 3.x
- No additional libraries are required as it only uses standard Python libraries (`os`, `shutil`, and `re`).

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory from where you want to start the search.
3. Run the script using the command:

```shell
   python macrophage.py
```

4. When the script starts, it will prompt you to enter the regex pattern to match folder names. For example:

```shell
Enter the regex pattern to match folder names (e.g., "node_modules"):
```

5. It will then search through all folders, and for each match, it will display the folder name and location, asking if you want to delete it:

```shell
Found node_modules in /path/to/parent/folder
Do you want to delete it? (y/n):
```

6. To delete the folder:

Press y or Y and hit Enter, or simply press Enter.
To keep the folder, press n and hit Enter.

## Example

If you enter the regex pattern node_modules, the script will find all folders named node_modules from the current directory and prompt you with each one it finds, giving you the option to delete it.

## Important Notes

Be careful when deleting folders, as this action is irreversible.
Ensure you have the necessary permissions to delete folders within the directory structure.

### License

This script is provided as-is, without any warranty. Use it at your own risk.
