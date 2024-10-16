# Scripts for `makedown` development

These scripts are used to develop `makedown`.

## [venv]() Create a virtual environment and install dependencies

```bash
rm -rf venv

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install setuptools
pip install wheel
pip install twine
pip install black
pip install python-dotenv
pip freeze > requirements.txt
```

## [format]() Format the source code

```bash
source venv/bin/activate

black makedown.py tests
npx prettier --print-width 80 --prose-wrap always --write "**/*.md"
```

## [test]() Run the tests

```bash
source venv/bin/activate

cd tests

MAKEDOWN_NO_WALK=TRUE MAKEDOWN_NO_COLOR=TRUE python test.py
```

## [build]() Build PyPI package

```bash
source venv/bin/activate

rm -rf build dist makedown.egg-info
python setup.py sdist bdist_wheel
```

## [pypi]() Publish the package to PyPI

```bash
source venv/bin/activate

./makedown.py build # Use local makedown
twine upload dist/*
```

# [eee]() EEE

```bash
export HELLO=WORLD

echo $HELLO
```

```bash
echo hello=$HELLO
```
