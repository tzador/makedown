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

    ```sh
    echo "Hello"
    ```

    # world

    ```js
    console.log("World");
    ```

    # generate-password

    ```python
    import random
    import string

    length = 8

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)
    ```

Run `x generate-password` to generate a random password.

# Command line completions for ZSH

Add the following to your `.zshrc`:

```zsh
# BEGIN XFile completions

function _x_completion {
  local -a options
  options=(${(f)"$(x __list_commands 2>/dev/null)"})
  _describe "choices" options
}

compdef _x_completion x

# END XFile completions
```
