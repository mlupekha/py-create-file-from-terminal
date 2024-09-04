import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    if not args:
        raise ValueError("No arguments provided")

    dir_path = []
    file_name = None

    if "-d" in args:
        d_flag = args.index("-d")
        if "-f" in args:
            f_flag = args.index("-f")
            dir_path = args[d_flag + 1:f_flag]
            file_name = args[f_flag + 1]
        else:
            dir_path = args[d_flag + 1:]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if dir_path:
        os.makedirs(os.path.join(*dir_path), exist_ok=True)

    if file_name:
        if dir_path:
            file_path = os.path.join(*dir_path, file_name)
        else:
            file_path = file_name

        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")
            line_number = 1
            while True:
                content = input(f"Enter content line {line_number}: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1


if __name__ == "__main__":
    create_file()
