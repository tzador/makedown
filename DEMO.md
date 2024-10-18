---
title: Blogging Like a Boss
author: me
---

Here are a few examples of commands:

## `welcome` - Prints a welcome message

By default bash is used as interpreter for the commands.

```
echo "Welcome to makedown.sh"
```

## `interpreter-chain` Choose a specific interpreter

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

```typescript
#!/usr/bin/env deno

const message: string = "step 4: I run in deno";
console.log(message);
```

### Some handy helpers

A set of handy file system helpers is available.

### `dirsize` Prints the total size of a directory

```bash
du -sh "$2"
```

### `find-files` Finds files in a directory recursively

```zsh
find "$1" -type f
```

### `kill-port` Kills a process listening on a port

```zsh
kill -9 $(lsof -t -i:$1)
```

### `prime-numbers` Prints the first 100 prime numbers

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

### `argv` command line arguments test

```python
#!/usr/bin/env python

import sys

print(sys.argv)
```
