# [makedown](https://github.com/tzador/makedown) - A Markdown-powered Makefile Alternative

Traditional tools like `Makefile` and `package.json` scripts are useful but
limited:

- **Makefiles** are excellent for task automation but lack support for embedding
  documentation or leveraging syntax highlighting.
- **package.json** scripts force you to write commands in one line, making
  complex commands harder to maintain.

**makedown** fills the gap by offering a simple, language-agnostic way to define
scripts within Markdown, complete with built-in documentation and the ability to
execute commands with ease.

![](./docs/screenshot.png)

- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
  - [Define Commands in Markdown](#define-commands-in-markdown)
  - [Running Commands](#running-commands)
  - [Command Dependencies](#command-dependencies)
  - [Viewing Available Commands](#viewing-available-commands)
  - [Example Directory Structure](#example-directory-structure)
- [Command Syntax](#command-syntax)
- [Example](#example)
- [Advanced Features](#advanced-features)
  - [Interpreter Aliases](#interpreter-aliases)
  - [Hierarchical Scanning](#hierarchical-scanning)
  - [Debug Mode](#debug-mode)
  - [No Color Mode](#no-color-mode)
- [Upgrading makedown](#upgrading-makedown)
- [Uninstall](#uninstall)
- [Contributing](#contributing)
- [License](#license)

`makedown` combines the power of Markdown documentation with the simplicity of
Makefiles, allowing you to embed and execute scripts directly from your `.md`
files. It's ideal for developers who want to keep documentation and scripts
side-by-side, while leveraging the clarity of markdown syntax highlighting. With
**makedown**, you can define and run commands in a variety of programming
languages, all from within your Markdown files.

---

## Key Features

- **Executable Markdown**: Embed executable commands within `.md` files and run
  them directly from the terminal.
- **Multilingual**: Support for multiple interpreters (`bash`, `zsh`, `python`,
  `javascript`, and more). You can use any interpreter with a simple shebang
  (`#!`).
- **Syntax Highlighting**: Markdown's code blocks are leveraged for clarity,
  making scripts more readable and maintainable.
- **Hierarchical Scanning**: Automatically find commands in Markdown files,
  starting from the current directory and walking up the directory tree.
- **Flexible Dependencies**: Define command dependencies to execute complex
  workflows by linking scripts together.

---

## Installation

Install **makedown** using `pip`:

```bash
pip install makedown
```

Once installed, you can use `makedown` from the command line to execute scripts
within your Markdown files.

---

## Usage

### Define Commands in Markdown

You can define commands within a Markdown file using headings and code blocks.
Here's an example:

````markdown
# scripts.md

## [greet]() Print a greeting message

This command prints "Hello, world!" using bash.

```bash
echo "Hello, world!"
```

## [farewell]() Print a farewell message using Python

```python
#!/usr/bin/env python
print("Goodbye, world!")
```
````

### Running Commands

To run a command defined in your Markdown file, use `makedown` followed by the
command name:

```bash
makedown greet
```

Alternatively, you can use a shorter alias:

```bash
m greet
```

### Command Dependencies

You can link commands together by specifying dependencies within parentheses
`()`. For example:

````markdown
## [build](clean) Build the project

This command builds the project, but first runs the `clean` command.

```bash
echo "Building project..."
```

## [clean]() Clean up project files

```bash
rm -rf build/
echo "Project cleaned."
```
````

Running `makedown build` will first execute the `clean` command, ensuring a
fresh build environment.

### Viewing Available Commands

To see a list of all available commands in your Markdown files:

```bash
makedown --help
```

You can also view details for a specific command by appending `--help` to the
command:

```bash
makedown greet --help
```

### Example Directory Structure

If you have a project structure like this:

```
/my-project
  |-- scripts.md
  |-- src/
  |-- README.md
```

You can define commands in `scripts.md` and run them from anywhere inside the
project directory or subdirectories. **makedown** will search for `.md` files
and find the commands.

---

## Command Syntax

Commands are defined using the following pattern in Markdown:

````
## [command-name](dependency1 dependency2) Description of the command

```language
command source code here
```
````

- **command-name**: The name of the command to be executed.
- **dependencies**: (Optional) A list of other commands that must run before
  this command.
- **Description**: A brief description of what the command does.
- **language**: The language/interpreter to be used (e.g., `bash`, `python`,
  `node`, etc.).

---

## Example

Here's a more complete example:

````markdown
# My Project's Commands

## [setup]() Set up the project environment

```bash
echo "Setting up project..."
pip install -r requirements.txt
```

## [test](setup) Run tests

```python
import unittest
unittest.main()
```

## [deploy](test) Deploy the project

```bash
echo "Deploying project to production..."
# Add your deployment script here
```
````

- Running `makedown deploy` will first execute the `test` command, which will,
  in turn, run the `setup` command.

---

## Advanced Features

### Interpreter Aliases

`makedown` supports many interpreters out of the box. You can specify the
interpreter using code block identifiers:

- `bash`, `sh`, `zsh` for shell scripts.
- `python`, `py` for Python scripts.
- `node`, `js` for JavaScript.

If you need to use a different interpreter, just include a shebang (`#!`) at the
top of your script, and `makedown` will respect it.

### Hierarchical Scanning

By default, `makedown` will scan for Markdown files in the current directory and
all parent directories, allowing you to organize your scripts across multiple
files.

You can turn off hierarchical scanning by setting the `MAKEDOWN_NO_WALK`
environment variable:

```bash
export MAKEDOWN_NO_WALK=TRUE
```

### Debug Mode

Enable debug mode to see additional logging information:

```bash
export MAKEDOWN_DEBUG=TRUE
```

### No Color Mode

If you prefer no color output in your terminal, you can disable it by setting:

```bash
export MAKEDOWN_NO_COLOR=TRUE
```

---

## Upgrading makedown

To upgrade to the latest version of **makedown**, run:

```bash
pip install --upgrade makedown
```

---

## Uninstall

If you wish to remove **makedown** from your system, use:

```bash
pip uninstall makedown
```

---

## Contributing

This is an open-source project, and contributions are welcome! If you have any
ideas, suggestions, or bug reports, feel free to open an
[issue](https://github.com/tzador/makedown/issues) or submit a
[pull request](https://github.com/tzador/makedown/pulls).

Join our [Discord](https://discord.gg/Gcr9H897zD) server to discuss new features
or get help using **makedown**.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE)
file for more information.
