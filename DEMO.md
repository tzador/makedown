---
cwd: .
env:
  - name: FOO
    value: BAR
  - file: .env
---

# Demo makedown file

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

```typescript
#!/usr/bin/env deno

const message: string = "step 4: I run in deno";
console.log(message);
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

### [prime-numbers]() Prints the first 100 prime numbers

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

### [weather]() Get current weather for a location

```bash
#!/bin/bash

location="$1"
if [ -z "$location" ]; then
  echo "Please provide a location."
  exit 1
fi

curl -s "wttr.in/$location?format=3"
```

### [generate-password]() Generate a secure random password

```python
#!/usr/bin/env python3

import string
import secrets

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

print(generate_password())
```

### [compress-images]() Compress images in a directory

```bash
#!/bin/bash

directory="$1"
if [ -z "$directory" ]; then
  echo "Please provide a directory path."
  exit 1
fi

find "$directory" -type f \( -iname "*.jpg" -o -iname "*.png" \) -print0 |
  xargs -0 -I {} convert {} -sampling-factor 4:2:0 -strip -quality 85 -interlace JPEG -colorspace RGB {}
```

### [count-lines]() Count lines of code in a directory

```python
#!/usr/bin/env python3

import os
import sys

def count_lines(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.html', '.css', '.md')):
                with open(os.path.join(root, file), 'r') as f:
                    total_lines += sum(1 for line in f if line.strip())
    return total_lines

if len(sys.argv) < 2:
    print("Please provide a directory path.")
    sys.exit(1)

directory = sys.argv[1]
print(f"Total lines of code: {count_lines(directory)}")
```
