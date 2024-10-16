#!/usr/bin/env python

import time
import sys
import re
import os

version = "0.0.4"

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
    "rb": "ruby",
    "ruby": "ruby",
    "pl": "perl",
    "perl": "perl",
    "php": "php",
    "lua": "lua",
    "tcl": "tclsh",
}


DEBUG = os.environ.get("MAKEDOWN_DEBUG") == "TRUE"
NO_COLOR = os.environ.get("MAKEDOWN_NO_COLOR") == "TRUE"
NO_WALK = os.environ.get("MAKEDOWN_NO_WALK") == "TRUE"


def red(text):
    if NO_COLOR:
        return text
    return f"\033[91m{text}\033[0m"


def green(text):
    if NO_COLOR:
        return text
    return f"\033[92m{text}\033[0m"


def blue(text):
    if NO_COLOR:
        return text
    return f"\033[94m{text}\033[0m"


def yellow(text):
    if NO_COLOR:
        return text
    return f"\033[93m{text}\033[0m"


def find_md_files():
    current_dir = os.getcwd()

    while True:
        files = os.listdir(current_dir)
        files.sort()

        found = False
        for file in files:
            if file.lower().endswith(".md"):
                yield os.path.abspath(os.path.join(current_dir, file))
                found = True

        if found and NO_WALK:
            break

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            break

        current_dir = parent_dir


class Command:
    def __init__(self, file, level, name, dependencies, description, source, line_number):
        self.file = file
        self.level = level
        self.name = name
        self.dependencies = dependencies
        self.description = description
        self.source = source
        self.line_number = line_number


def parse_md_file(file):
    commands = []
    with open(file, "r") as f:
        lines = [line.rstrip() for line in f.read().splitlines()]
        for line_number, line in enumerate(lines):
            match = re.match(r"^(#+)\s\[([^\]]+)\]\(([^\)]*)\)\s*(.*)$", line)
            if not match:
                continue

            source = re.split(
                r"^#", "\n".join(lines[line_number:]), flags=re.MULTILINE
            )[1].strip()

            commands.append(
                Command(
                    file=file,
                    level=len(match.group(1)),
                    name=match.group(2).strip(),
                    dependencies=re.split(r"\s+", match.group(3).strip()),
                    description=match.group(4).strip(),
                    source=source,
                    line_number=line_number + 1,
                )
            )

    return commands


def print_help():
    max_length = 0
    for file in find_md_files():
        for command in parse_md_file(file):
            if (command.name[0] == '-'):
                continue
            max_length = max(max_length, len(command.name))

    print("More info at https://github.com/tzador/makedown")
    print()
    for file in find_md_files():
        commands = parse_md_file(file)
        if len(commands) == 0:
            continue
        print(blue(file))
        print()
        for command in commands:
            if (command.name[0] == '-'):
                continue
            print(
                "$",
                green("makedown " + command.name) +
                (" " + " " * (max_length - len(command.name))+"    # " +
                 command.description if command.description else ""),
            )
        print()


def print_command_help(command_name):
    for file in find_md_files():
        commands = parse_md_file(file)
        for command in commands:
            if command.name != command_name:
                continue

            print(green("@ " + file))
            print()
            print(command.source)
            print()
            return

    print(red(f"Unknown command '{command_name}'"), file=sys.stderr)


def execute_dependencies(command, executed_commands=None):
    if executed_commands is None:
        executed_commands = set()

    for dep in command.dependencies:
        if dep and dep not in executed_commands:
            for file in find_md_files():
                for cmd in parse_md_file(file):
                    if cmd.name == dep:
                        execute_dependencies(cmd, executed_commands)
                        execute_command(cmd)
                        executed_commands.add(dep)
                        break
                else:
                    continue
                break
            else:
                print(red(f"Dependency '{dep}' not found for command '{
                      command.name}'"), file=sys.stderr)


def execute_command(command):
    execute_dependencies(command)

    for section in command.source.split("```")[1::2]:
        parts = section.split("\n", 1)

        alias = parts[0].strip()
        script = parts[1].strip() + "\n"

        interpreter = alias_to_interpreter.get(alias)

        if not interpreter and not script.startswith("#!"):
            print(red(f"Unknown interpreter for '{alias}'"), file=sys.stderr)
            return

        executable = command.file + "." + str(time.time())

        with open(executable, "w") as f:
            if not script.startswith("#!"):
                f.write("#!/usr/bin/env " + interpreter + "\n")
            f.write(script)

        os.chmod(executable, 0o755)

        try:
            os.system(executable + " " + " ".join(sys.argv[1:]))
        finally:
            os.remove(executable)
            pass


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print_help()
        return

    if len(sys.argv) >= 2 and sys.argv[1] == "--version":
        print("makedown:" + version)
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

    print(red(f"Unknown command '{command_name}'"), file=sys.stderr)


if __name__ == "__main__":
    main()
