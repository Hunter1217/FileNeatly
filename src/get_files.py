from pathlib import Path
import re

def get_home_dir():
    home_dir = Path.home()
    return home_dir

def get_sub_dirs(parent_path):
    files = []
    sub_dirs = []
    for x in parent_path.iterdir():
        if x.is_dir():
            sub_dirs.append(x)
        elif x.exists():
            files.append(x)
    # sub_dirs = [x for x in parent_path.iterdir() if x.is_dir()]
    return sub_dirs, files

def main():
    home_dir = get_home_dir()
    check_path = Path('/Users/hunte/OneDrive/Documents')
    sub_dirs, files = get_sub_dirs(check_path)
    print(f"The Home Directory is {home_dir}")
    for name in sub_dirs:
        print(f"Directorys: {name}")

    for file in files:
        print(f"Files: {file}")
        if file.suffix == ".txt":
            with open(file) as f:
                print(f"This is a line from the file {file}: {f.readline()}")


if __name__ == "__main__":
    main()