#!/usr/bin/env python

import os

def find_md_files():
    current_dir = os.getcwd()

    while True:
        files = os.listdir(current_dir)
        files.sort()

        for file in files:
            if file.lower().endswith('.md'):
                yield os.path.abspath(os.path.join(current_dir, file))

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            break

        current_dir = parent_dir

for file in find_md_files():
    print("@", file)
