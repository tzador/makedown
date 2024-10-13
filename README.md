# XFile

`xfile` is a CLI tool that allows you to run shell commands, JavaScript code, and Python code from a single or multiple files.

Think of it as alternative to `Makefile` and `package.json` scripts.

Out of the box syntax highlighting due to markdown code blocks.

# Installation

```zsh
npm install -g @tzador/xfile
```

# Usage

Create a file named `x.md` in your project root, with the following example content:

    <!-- /path/to/my/project/x.md -->

    # hello

    Prints "Hello" to `stdout` using Zsh.

    ```zsh
    echo "Hello"
    ```

    # world

    Just prints "World" to `stdout` using JavaScript.

    ```js
    console.log("World");
    ```

    # generate-password

    Prints a random password to `stdout` using Python.

    ```python
    import random
    import string

    length = 16

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)
    ```

Run `x generate-password` to generate a random password.

# Command line completions for ZSH

Run the following once to add `x` command completions to your `.zshrc`:

```zsh
x --zsh-completion >> ~/.zshrc
```

Then restart your terminal.

It will suggest available commands when you type `x` and press tab.
