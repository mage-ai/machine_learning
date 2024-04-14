import os

from mage_ai.settings.repo import get_variables_dir

if 'condition' not in globals():
    from mage_ai.data_preparation.decorators import condition


def count_files_with_prefix(directory, prefix):
    """
    Recursively count the number of files within the specified directory and all its subdirectories
    that start with the given prefix.

    Args:
    - directory (str): The path to the root directory to start search.
    - prefix (str): The prefix to search for in file names.

    Returns:
    - int: The count of files with names starting with the prefix.
    """
    count = 0  # Initialize a counter
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f'The directory {directory} does not exist.')
        return count
    
    # Walk through all directories and files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name starts with the specified prefix
            if file.startswith(prefix):
                count += 1
    
    return count


@condition
def evaluate_condition(*args, **kwargs) -> bool:
    directory_path = os.path.join(
        get_variables_dir(), 
        'pipelines',
        'core_data_users_v0',
        '.variables',
    )
    prefix = 'data.parquet'
    file_count = count_files_with_prefix(directory_path, prefix)

    return file_count % 4 == 0
