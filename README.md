# makedown.sh

`makedown.sh` is a versatile CLI tool that lets you execute shell scripts,
JavaScript code, and Python code from one or more markdown files.
It's a streamlined alternative to `Makefile` or `package.json` scripts,
and it features built-in syntax highlighting through markdown code blocks.

## Key Features

- Multilingual Execution: Supports Zsh, JavaScript, and Python.
- Simplified Scripting: Use markdown files (.md) to organize and run commands.
- Syntax Highlighting: Leverages markdown code blocks for readability.
- Autocomplete Support: ZSH completions for a smoother workflow.

## Install

```bash
npm install -g makedown.sh
```

## Usage

Define and document your commands in a markdown file, like [DEMO.md](./DEMO.md).

Then use `makedown.sh` to run them, from within the same directory or any subdirectory.

```bash
makedown.sh --help # Prints help with available commands
makedown.sh # Also prints help

makedown.sh my_command # Runs the command
makedown.sh my_command arg1 arg2 # Pass arguments to the command
makedown.sh my_command --help # Prints help for the command
```
