import os

def remove_hash_from_mp4(directory):
    """
    Recursively goes through a directory and removes the '#' symbol
    from .mp4 filenames.

    Args:
        directory (str): The path to the directory to process.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".mp4") and "#" in filename:
                old_filepath = os.path.join(root, filename)
                new_filename = filename.replace("#", "").strip()
                new_filepath = os.path.join(root, new_filename)
                try:
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed: '{filename}' to '{new_filename}'")
                except OSError as e:
                    print(f"Error renaming '{filename}': {e}")

if __name__ == "__main__":
    target_directory = r"G:\Tech tutorials\LeetCode In Python 50 Algorithms Coding Interview Questions\[TutsNode.com] - LeetCode In Python 50 Algorithms Coding Interview Questions"
    remove_hash_from_mp4(target_directory)
    print("Finished processing the directory.")