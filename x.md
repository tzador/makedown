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
