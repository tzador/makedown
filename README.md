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

## [welcome]() Welcome message

By default bash is used as interpreter for the commands.

```
echo "Welcome to makedown.sh"
```

## [interpreter-chain]() Choose a specific interpreter

When several tripple backtick code blocks are present, they are executed in order.

```sh
echo I run in sh
```

```bash
echo I run in bash
```

```zsh
echo I run in bash
```

```python
print("I run in python")
```

```javascript
console.log("I run in node");
```

### Some handy helpers

A set of handy file system helpers is available.

### [dirsize]() Prints the total size of a directory

```bash
du -sh "$1"
```

### [find-files]() Finds files in a directory recursively

```zsh
find "$1" -type f
```

### [kill-port]() Kills a process listening on a port

```zsh
kill -9 $(lsof -t -i:$1)
```
