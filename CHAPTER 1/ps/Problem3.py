import os

def list_directory_contents(path):
    try:
        entries = os.listdir(path)
    except Exception as e:
        print(f"Error: {e}")
        return

    print("All entries (files + directories):")
    for name in entries:
        print(name)

    # If you want only files (not subdirectories):
    files = [name for name in entries
             if os.path.isfile(os.path.join(path, name))]

    print("\nOnly files:")
    for fname in files:
        print(fname)


if __name__ == "__main__":
    dir_path = input("Enter directory path: ").strip()
    list_directory_contents(dir_path)
