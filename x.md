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

length = 16

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)
```
