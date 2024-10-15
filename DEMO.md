# DEMO.md

Here are a few examples of commands:

## [welcome]() Welcome message

By default bash is used as interpreter for the commands.

```
echo "Welcome to makedown.sh"
```

## [interpreter-chain]() Choose a specific interpreter

When several tripple backtick code blocks are present, they are executed in order.

```sh
echo "I run in sh"
```

```bash
echo "I run in bash"
```

```zsh
echo "I run in zsh"
```

```python
#!/opt/homebrew/bin/python
print("I run in python")
```

```javascript
#!/opt/homebrew/bin/node
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
