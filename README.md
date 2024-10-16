# [makedown]() - A Markdown powered Makefile alternative

`makedown` (aka Makefile + Markdown) is motivated by developers need to define
multiple scripts in one file next to their documentation, and have a handy way
to run them from terminal.

`Makefile`s are great for this, but are lucking some of the
[`makedown`](https://github.com/tzador/makedown) features, such as syntax
highlighting, hierarchical scanning of .md files with embedded documentation.

There are also `package.json` scripts in `node.js` world, but users are forced
to write script commands in one line.

It is implemented in Python for portability reasons, since most Unix-like
systems already have a Python interpreter installed.

Here is [DEMO.md](./DEMO.md) file with examples of usage.

---

This is a fresh project still under active development.

Feel free to open and [issue](https://github.com/tzador/makedown/issues) or
[PR](https://github.com/tzador/makedown/pulls).

We also have have a [Discord server](https://discord.gg/Gcr9H897zD) for quick
discussions and sharing ideas or feedback.

---

## Key Features

- **Executable Markdown Scripting**: Use markdown files (.md) to organize
  commands and their documentation.
- **Multilingual Execution**: Supports `zsh`, `bash`, `javascript`, `python` and
  **infinitely** many more, using custom hashbangs.
- **Syntax Highlighting**: Leverages markdown code blocks for readability.

---

## Install

```bash
pip install makedown
```

## Use

Define commands in a `.md` file:

````markdown
# my_scripts.md

Here are a few examples of commands:

## [hello]() Prints "hello" using bash

```bash
echo "hello"
```

## [world]() Prints "world" using python

This is a more detailed description of the command.

```python
#!/usr/bin/env python

echo "world"
```
````

To run commands in a markdown file, execute `makedown` from the same directory
or any subdirectory:

```bash
makedown hello
```

A shorter version is also available:

```bash
m world
```

To see all the available commands with their short descriptions, use one of the
following:

```bash
makedown --help
```

or just run it without any arguments:

```bash
m
```

To get more details about a specific command, use:

```bash
makedown world --help
```

## Upgrade

```bash
pip install --upgrade makedown
```

## Uninstall

```bash
pip uninstall makedown
```
