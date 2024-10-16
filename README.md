# [makedown]() - A Markdown powered Makefile alternative

`makedown` (aka Makefile + Markdown) is motivated by developers need to define
multiple scripts in one file next to their documentation, and have a handy way
to trigger them from terminal.

`Makefile`s are great for this, but are lucking some of the
[`makedown`](https://github.com/tzador/makedown) features, such as syntax
highlighting, hierarchical scanning and embedded documentation.

There are also `package.json` scripts in `node.js` world, but users are forced
to write script commands in one line.

It is implemented in Python for portability reasons, since most Unix-like
systems already have a Python interpreter installed.

## Key Features

- [x] **Executable Markdown Scripting**: Use markdown files (.md) to organize
      commands and their documentation.
- [x] **Multilingual Execution**: Supports `zsh`, `bash`, `javascript`, `python`
      and **infinitely** many more.
- [x] **Syntax Highlighting**: Leverages markdown code blocks for readability.
- [x] **Flexible Code Blocks**: Support for triple backtick code blocks.
- [ ] **Autocomplete Support**: ZSH completions for a smoother workflow.

## How to use

### Install

```bash
pip install makedown
```

### Define commands in a `.md` file

````markdown
# my_scripts.md

Here are a few examples of commands:

## [hello]() Prints a welcome message

```bash
echo "hello, world!"
```
````

### Executing commands

To run commands in a markdown file, execute `makedown` from the same directory
or any subdirectory:

```bash
makedown hello
```

A shorter version is also available:

```bash
m hello
```

### Printing help

To see all the available commands with their documentation, use one of the
following:

```bash
makedown --help
```

or just run it without any arguments:

```bash
makedown # just `m` also works
```

### Using other languages

```python
print("hello, world!")
```

### Upgrade

```bash
pip install --upgrade makedown
```

### Uninstall

```bash
pip uninstall makedown
```

---

## DEMO.md

````markdown
Here are a few examples of commands:

## [welcome]() Prints a welcome message

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
du -sh "$2"
```

### [find-files]() Finds files in a directory recursively

```zsh
find "$1" -type f
```

### [kill-port]() Kills a process listening on a port

```zsh
kill -9 $(lsof -t -i:$1)
```

```ruby
#!/usr/bin/env ruby

def is_prime?(number)
  return false if number <= 1
  (2..Math.sqrt(number)).none? { |i| number % i == 0 }
end

def first_n_primes(n)
  primes = []
  number = 2
  while primes.length < n
    primes << number if is_prime?(number)
    number += 1
  end
  primes
end

# Print the first 100 prime numbers
first_100_primes = first_n_primes(100)
puts first_100_primes
```

### [argv]() command line arguments test

```python
#!/usr/bin/env python

import sys

print(sys.argv)
```
````
