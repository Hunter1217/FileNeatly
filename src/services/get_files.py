from pathlib import Path

def get_home_dir():
    home_dir = Path.home()
    return home_dir

def get_sub_dirs(parent_path):
    print("DEBUG get_sub_dirs type:", type(parent_path), "value:", parent_path)

    # if not isinstance(parent_path, Path):
    #     raise TypeError(f"get_sub_dirs expected pathlib.Path got {type(parent_path)}")
    files = []
    sub_dirs = []

    try:
        for x in parent_path.iterdir():
            try:
                if x.is_dir():
                    sub_dirs.append(x)
                elif x.is_file():
                    files.append(x)
            except PermissionError:
                continue
    except PermissionError:
        return [], []
    except Exception as e:
        print("Exception:" , e)
        return [], []
    return sub_dirs, files


def change_dirs_loop(home_dir=get_home_dir()):
    command = ""
    # check_path = Path('/Users/hunte/OneDrive/Documents')\
    check_path = home_dir
    old_paths = [check_path]
    while(command != "exit"):
        print(f"Current Directory: {check_path}")
        sub_dirs, files = get_sub_dirs(check_path)

        if not sub_dirs and not files:
            print("Empty Directory")
            check_path = old_paths.pop()
            continue

        dict_of_dirs = {index + 1: value for index, value in enumerate(sub_dirs)}
        dict_of_files = {index + 1: value for index, value in enumerate(files)}
        
        try:
            file_or_dir = input("Type f to check files, type d to check directories, or type . to go to the previous directory: ")
            file_or_dir = file_or_dir.lower()
            print(f"check file or dir: {file_or_dir}")
            if file_or_dir == "f":
                for num, file in dict_of_files.items():
                    print(f"Options of Files in the directory {check_path}: {num}: {file}")
                continue
                # num_input = int(input("What file would you like to go to? "))
                # print(f"File extraction: {dict_of_files[num_input]}")
                # old_path = check_path 
                # check_path = Path(dict_of_files[num_input])
            elif file_or_dir == "d":
                if not dict_of_dirs:
                    print("This directory has no directories, try again")
                    continue
                for num, my_dirs in dict_of_dirs.items():
                    print(f"Options of directories to change to: {num}: {my_dirs}")
                num_input = int(input("What directory would you like to go to? "))
                print(f"Directory extraction: {dict_of_dirs[num_input]}")
                old_paths.append(check_path)
                check_path = Path(dict_of_dirs[num_input])
            elif file_or_dir == ".":
                if not old_paths:
                    check_path = home_dir
                    continue
                check_path = old_paths.pop()
                continue
            else:
                print("Incorrect input, try again.")
        except Exception as e:
            print("Exception: ", e)
            break


def main():
    home_dir = get_home_dir()
    change_dirs_loop(home_dir)
    print(f"The Home Directory is {home_dir}")

if __name__ == "__main__":
    main()