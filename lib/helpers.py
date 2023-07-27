import os

# Check if the file 'phase3_database.db' exists in the current working directory
if os.path.exists('phase3_database.db'):
    print("'phase3_database.db' exists in the current working directory.")
else:
    print("'phase3_database.db' does not exist in the current working directory.")
