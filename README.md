# [makedown](https://makedown.dev) - Markdown + Makefile = Self documenting shell scripts

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

````
# Example makedown file
                                        $ makedown --help                      # List available commands
                                        hello
                                        world

## hello-command # Prints "hello"       $ makedown command
                                        hello

More details about the command.         $ m hello-command                      # a short `m` alias
                                        hello
```bash
printf "hello"
```

### world-command # Print "hello world" $ m wor<HIT TAB>ld-command             # Bash/Zsh autocomplete

- hello # hello is run beforehand

More details about the command.         $ m -h world-command                   # Full command help

```python
print("wolrd")
```
````
