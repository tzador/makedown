# Just a demo x.md file

This text here is ignored, just for documentation purposes.

## hello

Prints "Hello" to `stdout` using Zsh.

```zsh
echo "Hello"
```

## world

Just prints "World" to `stdout` using JavaScript.

```js
console.log("World");
```

## weather-tomorrow

Prints the weather for tomorrow to `stdout` using Zsh.

```zsh
curl wttr.in/tomorrow
```

## generate-password

Prints a random password to `stdout` using Python.

```python
import random
import string

length = 16

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)
```
