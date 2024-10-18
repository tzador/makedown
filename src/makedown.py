#!/usr/bin/env python

import os
import re
import sys

version = "0.1.0"

def print_commands():
    print("https://makedown.dev")


def main():
    my_args = []

    print(sys.argv)
    for arg in sys.argv[1:]:
        print(arg)
        if not arg.startswith("-"):
            break
        my_args.append(arg)

    if len(my_args) == 0 or my_args[0] == "--help" or my_args[0] == "-h":
        print_commands()
        exit(1)

if __name__ == "__main__":
    main()
