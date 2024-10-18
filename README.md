# [makedown](https://makedown.dev) - Markdown + Makefile = Self documenting shell scripts

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!--
    adsf
    asdf
    asdf
    asdf
    asdf
    asdf
    asdf
    adsf
    asd
    asdf
    asd
    dsaf
    adsf
    dsaf
    dfsa
-->

<!-- GENERATED START -->
<div style="
font-family: monospace;
background-color: #f0f0f0;
padding: 0.5rem 0;
border: 1px solid #e0e0e0;
border-radius: 0.5rem;
display:flex;
flex-direction: column;
line-height: 1.5;
">

<h1 style="line-height: 1.5; font-size: 1.5rem; font-weight: bold; background: #e0e0e0; padding: 0 1rem"># Example README.md</h1>
<div style="line-height: 1.5;">&nbsp;</div>
<div style="background: #e0e0e0;">This file is contains runnable commands.</div>
<div style="font-weight: bold; background: #e0e0e0; padding: 0 1rem">## world # Says "hello world"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="background: #303030"><div style="color: dodgerblue; display: inline-block">$</span> makedown world</div></div>
<div style="display: grid; grid-template-columns: 1fr 1fr;">
<div style="background: #f0f0f0; padding: 0 1rem">world</div>
<div style="background: #404040; padding: 0 1rem; padding-left: 1rem; color: white">hello</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr;">
<div style="background: #f0f0f0; padding: 0 1rem">world</div>
<div style="background: #404040; padding: 0 1rem; padding-left: 1rem; color: white">hello</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr;">
<div style="background: #f0f0f0; padding: 0 1rem">world</div>
<div style="background: #404040; padding: 0 1rem; padding-left: 1rem; color: white">hello</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr;">
<div style="background: #f0f0f0; padding: 0 1rem">world</div>
<div style="background: #404040; padding: 0 1rem; padding-left: 1rem; color: white">hello</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr;">
<div style="background: #f0f0f0; padding: 0 1rem">world</div>
<div style="background: #404040; padding: 0 1rem; padding-left: 1rem; color: white">hello</div>
</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;depends on:</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;- hello</div>
<div>&nbsp;</div>
<div>```python</div>
<div>print("world")</div>
<div>```</div>
<div>&nbsp;</div>
<h2 style="font-size: 1.125rem; font-weight: bold;">### hello # Says "hello"</h2>
<div>&nbsp;</div>
<div>```bash</div>
<div>printf "hello "</div>
<div>```</div>
</div>
<!-- GENERATED END -->

---

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

We also have have a [Discord](https://discord.gg/Gcr9H897zD) server for quick
discussions and sharing ideas or feedback.

---

#h2ey Feath2s

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

print("world")
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
