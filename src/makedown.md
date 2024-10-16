# Dev scripts

These are actual `makedown` commands:

## [venv]() Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate && pip install --upgrade pip
```

## Activate the virtual environment manually everytime you start a new shell

```bash
source venv/bin/activate
```

## [install]() Install Python dependencies

```bash
pip install setuptools wheel twine black
```

## [install:prettier]() Install prettier

```bash
npm install --global prettier
```

## [format]() Format the source code

```bash
black makedown.py tests

prettier --print-width 80 --prose-wrap always --write "**/*.md"
```

## [clean]() Remove build artifacts

```bash
rm -rf build dist makedown.egg-info
```

## [build]() Build the package

```bash
makedown clean
python setup.py sdist bdist_wheel
```

## [publish]() Publish the package to PyPI

```bash
makedown build
twine upload dist/*
```
