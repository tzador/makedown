#!/usr/bin/env python

# TODO

# `$ makedown - -help-server` to start a local web server with the help docs
# bash/zsh completions
# colored output
# correct line numbers in error messages
# correct file paths in error messages
# when hashbang is present, use that
# do not show in --help the commands that start with _
# when command is misstyped, output the similar available commands
# allow ~/makdown.md file to specify global commands
# add a man page
# print license with --license
# use `.env` files
# add a --version flag
# add a --debug flag
# add a --no-color flag
# add

import time
import sys
import re
import os

alias_to_interpreter = {
    "": "bash",
    "bash": "bash",
    "zsh": "zsh",
    "sh": "sh",
    "shell": "sh",
    "js": "node",
    "javascript": "node",
    "py": "python",
    "python": "python",
    # TODO: add more aliases, like deno, bun, etc.
}

interpreter_to_extension = {
    "zsh": "zsh",
    "sh": "sh",
    "bash": "bash",
    "node": "mjs",
    "python": "py"
}


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
    def __init__(self, file, name, title, level, source, line_number):
        self.file = file
        self.name = name
        self.title = title
        self.level = level
        self.source = source
        self.line_number = line_number


def parse_md_file(file):
    commands = []
    with open(file, 'r') as f:
        lines = [line.rstrip() for line in f.read().splitlines()]
        for line_number, line in enumerate(lines):
            match = re.match(r'^#+\s\[([^\]]+)\]\(\)(.*$)', line)

            if not match:
                continue
            level = len(line.split(" ")[0])
            source = re.split(
                r'^#+\s', '\n'.join(lines[line_number:]), flags=re.MULTILINE)[1].strip()
            commands.append(Command(file=file,
                                    name=match.group(1).strip(),
                                    title=match.group(2).strip(),
                                    level=level,
                                    source=source, line_number=line_number + 1))

    return commands


def print_help():
    max_length = 0
    for file in find_md_files():
        for command in parse_md_file(file):
            max_length = max(max_length, len(command.name))

    print()
    for file in find_md_files():
        commands = parse_md_file(file)
        if len(commands) == 0:
            continue
        print('@  ', file)
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
    print(f"Unknown command '{command_name}'", file=sys.stderr)


def execute_command(command):
    for section in command.source.split("```")[1::2]:
        parts = section.split("\n", 1)

        alias = parts[0].strip()
        script = parts[1].strip() + "\n"

        interpreter = alias_to_interpreter.get(alias)

        if not interpreter:
            print(f"Unknown interpreter for '{alias}'", file=sys.stderr)
            return

        extension = interpreter_to_extension[interpreter]

        executable = command.file + "." + str(time.time()) + "." + extension

        with open(executable, "w") as f:
            f.write("#!/usr/bin/env " + interpreter + "\n")
            f.write(script)

        os.chmod(executable, 0o755)

        try:
            os.system(executable + " " + " ".join(sys.argv[1:]))
        finally:
            os.remove(executable)


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print_help()
        return

    if len(sys.argv) == 3 and sys.argv[2] == "--help":
        print_command_help(sys.argv[1])
        return

    command_name = sys.argv[1]
    for file in find_md_files():
        for command in parse_md_file(file):
            if command.name == command_name:
                execute_command(command)
                return

    print(f"Unknown command '{command_name}'", file=sys.stderr)


if __name__ == "__main__":
    main()
