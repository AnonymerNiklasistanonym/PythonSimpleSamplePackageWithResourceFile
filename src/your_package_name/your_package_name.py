#!/usr/bin/env python3

# Internal packages
import os.path

# Installed packages (via pip)
import genanki
import markdown


def main():
    print("your_package_name.py main method was called")
    print(f"{markdown.__version__=}")
    print(f"{genanki.__version__=}")

    with open("resource_file.txt", "r", encoding="utf-8") as f:
        resource_file_content = f.read()
        print(f"{resource_file_content=}")


# Main method (This will not be executed when file is imported)
if __name__ == "__main__":
    main()
