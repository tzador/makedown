# makedown - A Markdown powered Makefile alternative

```bash
pip install makedown
```

`makedown` is a versatile CLI tool that lets you execute shell scripts,
JavaScript code, Python code, or any other script defined in one or more markdown files.

It's a streamlined alternative to `Makefile`, `package.json`, or scattered shell scripts,
featuring built-in syntax highlighting through markdown code blocks and
allowing documentation of commands in a human-friendly format.

## Key Features

- **Multilingual Execution**: Supports Zsh, JavaScript, and Python.
- **Simplified Scripting**: Use markdown files (.md) to organize and run commands.
- **Syntax Highlighting**: Leverages markdown code blocks for readability.
- **Autocomplete Support**: ZSH completions for a smoother workflow.
- **Flexible Code Blocks**: Support for triple backtick code blocks.

## Installation

## Usage

1. Define and document your commands in a markdown file, like in [DEMO.md](./DEMO.md).
2. Run commands using `makedown` from the same directory or any subdirectory:

```bash
makedown --help  # Prints help with available commands
makedown         # Also prints help

makedown my_command           # Runs the command
makedown my_command arg1 arg2 # Pass arguments to the command
makedown my_command --help    # Prints help for the command
```

## Development

These are actual `makedown` commands:

### [venv]() Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate && pip install --upgrade pip
```

### Activate the virtual environment manually everytime you start a new shell

```bash
source venv/bin/activate
```

### [install]() Install Python dependencies

```bash
pip install setuptools wheel twine black
```

### [format]() Format the source code

```bash
black makedown.py
```

### [build]() Build the package

```bash
rm -rf build dist makedown.egg-info
python setup.py sdist bdist_wheel
```

### [publish]() Publish the package to PyPI

```bash
makedown build
twine upload dist/*
```
