# makedown.sh

`x.md` is a versatile CLI tool that lets you execute shell scripts,
JavaScript code, and Python code from one or more markdown files.
It's a streamlined alternative to `Makefile` or `package.json` scripts,
and it features built-in syntax highlighting through markdown code blocks.

## Key Features

- Multilingual Execution: Supports Zsh, JavaScript, and Python.
- Simplified Scripting: Use markdown files (.md) to organize and run commands.
- Syntax Highlighting: Leverages markdown code blocks for readability.
- Autocomplete Support: ZSH completions for a smoother workflow.

## Installation

```zsh
# TODO
```

## Usage

```
# TODO
```

Then restart your terminal.

It will suggest available commands when you type `x` and press tab.

# An example of a makedown file

To define commands put them under a level 2 header or above while defining the command name.

---

Here are a few examples of commands:

## [hello]() Prints a greeting

```
echo "Hello, world!"
```

### File system helpers

A set of handy file system helpers is available.

### [dirsize]() Prints the total size of a directory

```bash
du -sh "$1"
```

### [find-files]() Finds files in a directory recursively

```zsh
find "$1" -type f
```

## [several-scripts]() Several scripts

```sh
echo hello
```

```
echo world
```
