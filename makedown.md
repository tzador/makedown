# dev scripts

These scripts are used to develop `makedown`.

## [environment]() Create a virtual environment and install dependencies

````bash
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate && pip install --upgrade pip
    source venv/bin/activate && pip install setuptools wheel twine black
    npm install --global prettier


## [format]() Format the source code

```bash
black makedown.py tests
prettier --print-width 80 --prose-wrap always --write "**/*.md"
````

## [build]() Build PyPI package

```bash
rm -rf build dist makedown.egg-info
python setup.py sdist bdist_wheel
```

## [publish]() Publish the package to PyPI

```bash
makedown build
twine upload dist/*
```
