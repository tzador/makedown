#!/usr/bin/env python

import os
import re
import sys

version = "0.1.0"


class Section:
    def __init__(self, path, line_number, header, source, name, dependencies):
        self.path = path
        self.line_number = line_number
        self.header = header
        self.source = source
        self.name = name
        self.dependencies = dependencies
        if (header == "__I_AM_ROOT__"):
            self.depth = 0
        else:
            self.depth = len(header.split()[0])
        self.parent = None
        self.children = []
        self.subcommands = 0

    def __str__(self):
        return f"""\
{self.header}
{self.source}
| depth = {self.depth}
| name = {self.name}
| dependencies = {self.dependencies}
| path = {self.path}
| line_number = {self.line_number}
"""


def print_help():
    print("Usage: makedown [*options] [command] [*args]")

    print("Options:")
    print("  -h, --help      Show help")
    print("  -v, --version   Show version")

    print("Commands:")
    print("  build           Build the project")
    print("  compile         Compile the project")
    print("  docker-build    Build the Docker image")
    print("  docker-run      Run the Docker image")
    print("  clean           Clean the project")


def find_markdown_files():
    dir = os.getcwd()
    while True:
        for file in sorted(os.listdir(dir)):
            if file.lower().endswith(".md"):
                full_path = os.path.abspath(os.path.join(dir, file))
                yield full_path
                if file.lower().endswith("_.md"):
                    return
        parent = os.path.dirname(dir)
        if parent == dir:
            break
        dir = parent


def find_sections(path):
    root = Section(
        path=path,
        line_number=0,
        header="__I_AM_ROOT__",
        source="",
        name=None,
        dependencies=[],
    )

    stack = [root]

    with open(path, "r") as file:
        markdown = file.read()
        lines = markdown.splitlines()
        line_number = 0
        while line_number < len(lines):
            line = lines[line_number]
            if line.startswith("#"):
                splitted = line.split()
                if splitted[1].startswith("@"):
                    name = splitted[1][1:]
                    if name.endswith(":"):
                        name = name[:-1]
                    dependencies = splitted[2:]
                else:
                    name = None
                    dependencies = None

                next_section_start = line_number + 1
                while next_section_start < len(lines) and not lines[
                    next_section_start
                ].startswith("#"):
                    next_section_start += 1

                source = "\n".join(lines[line_number + 1 : next_section_start])

                section = Section(
                    path=path,
                    line_number=line_number + 1,
                    header=line,
                    source=source,
                    name=name,
                    dependencies=dependencies,
                )

                while len(stack) > 0 and stack[-1].depth >= section.depth:
                    stack.pop()

                stack[-1].children.append(section)
                section.parent = stack[-1]
                stack.append(section)

                if section.name is not None:
                    p = section.parent
                    while p is not None:
                        p.subcommands += 1
                        p = p.parent

                yield section

                line_number = next_section_start - 1
            line_number += 1


def print_commands():
    # TODO: show only the sections that have a command in them
    for path in find_markdown_files():
        for section in find_sections(path):
            # if section.subcommands > 0 or section.name is not None:
            print(section.header,  section.subcommands)


def run_command(command):
    pass


def main():
    args = sys.argv[1:]

    my_args = []
    your_args = []

    while len(args) > 0:
        arg = args.pop(0)
        if not arg.startswith("-"):
            your_args.append(arg)
            break
        my_args.append(arg)

    your_args.extend(args)

    if len(my_args) == 1 and (my_args[0] == "--help" or my_args[0] == "-h"):
        print_commands()
        exit(0)

    if len(my_args) == 1 and (my_args[0] == "--version" or my_args[0] == "-v"):
        print(version)
        exit(1)

    if len(my_args) != 0:
        print("Unknown options", my_args)
        exit(1)

    if len(your_args) == 0:
        print("TODO: run default command")
    else:
        print("TODO: run command", your_args)


if __name__ == "__main__":
    main()
