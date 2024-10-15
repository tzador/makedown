#!/usr/bin/env python

import os
import re
import sys


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


class Command:
    def __init__(self, path, name, title, level, source, number):
        self.path = path
        self.name = name
        self.title = title
        self.level = level
        self.source = source
        self.number = number


def parse_md_file(path):
    commands = []
    with open(path, 'r') as file:
        lines = [line.rstrip() for line in file.read().splitlines()]
        for number, line in enumerate(lines):
            match = re.match(r'^#+\s\[([a-zA-Z0-9_-]+)\]\(\)(.*$)', line)

            if not match:
                continue
            level = len(line.split(" ")[0])
            source = re.split(
                r'^#+\s', '\n'.join(lines[number:]), flags=re.MULTILINE)[1].strip()
            commands.append(Command(path=path,
                                    name=match.group(1).strip(),
                                    title=match.group(2).strip(),
                                    level=level,
                                    source=source, number=number + 1))

    return commands


def print_help():
    max_length = 0
    for file in find_md_files():
        commands = parse_md_file(file)
        for command in commands:
            max_length = max(max_length, len(command.name))

    print()
    for file in find_md_files():
        commands = parse_md_file(file)
        if len(commands) == 0:
            continue
        print('@', file)
        print()
        for command in commands:
            print('    ' + command.name + ' ' *
                  (max_length - len(command.name)), '-', command.title)
        print()


def print_command_help(command_name):
    for file in find_md_files():
        commands = parse_md_file(file)
        for command in commands:
            if command.name == command_name:
                print('@', file)
                print()
                print(command.source)
                print()
                return
    print("Unknown command")


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print_help()
        return

    if len(sys.argv) == 3 and sys.argv[2] == "--help":
        print_command_help(sys.argv[1])
        return

    print("Unknown command")


if __name__ == "__main__":
    main()
