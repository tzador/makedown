.PHONY: all clean .venv format test package publish upgrade

clean: # Clean the project
	rm -rf build dist makedown.egg-info
	rm -rf .venv

venv: clean # Create a virtual environment and install dependencies
	rm -rf .venv
	python3 -m venv .venv
	source .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install setuptools wheel twine black

format: # Format the source code
	source .venv/bin/activate && \
	black makedown.py tests && \
	npx prettier --print-width 80 --prose-wrap always --write "**/*.md"

test: # Run the tests
	source .venv/bin/activate
	cd tests && MAKEDOWN_NO_WALK=TRUE MAKEDOWN_NO_COLOR=TRUE python test.py

package: clean # Build PyPI package
	source .venv/bin/activate
	python setup.py sdist bdist_wheel


publish: package # Publish the package to PyPI
	source .venv/bin/activate
	./makedown.py build # Use local makedown
	twine upload dist/*

upgrade: #Upgrade the local installation
	pip uninstall makedown -y
	pip install makedown
