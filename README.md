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
- support tripple backtick code blocks

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

## DEMO.md

````markdown
# DEMO.md

Here are a few examples of commands:

## [welcome]() Welcome message

By default bash is used as interpreter for the commands.

```
echo "Welcome to makedown.sh"
```

## [interpreter-chain]() Choose a specific interpreter

When several code blocks are present, they are executed in order.

```sh
echo "step 1: I run in sh"
```

```bash
echo "step 2: I run in bash"
```

```zsh
echo "step 3: I run in zsh"
```

```python
#!/opt/homebrew/bin/python
print("step 4: I run in python")
```

```javascript
#!/opt/homebrew/bin/node
console.log("step 5: I run in node");
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
````
