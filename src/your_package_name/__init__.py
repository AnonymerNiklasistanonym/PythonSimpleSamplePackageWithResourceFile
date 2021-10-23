#!/usr/bin/env python3

#import your_package_name
from your_package_name.your_package_name import main as main_method


def main_init():
    print("__init__.py main method was called without any package references")

def main():
    main_method()
