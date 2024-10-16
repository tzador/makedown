from setuptools import setup

setup(
    name="makedown",
    version="0.0.0",
    py_modules=['makedown'],
    entry_points={
        'console_scripts': [
            'makedown=makedown:main',
        ],
    },
    install_requires=[
        # List of dependencies
    ],
    author="Tim Zadorozhny",
    author_email="tzador@gmail.com",
    description="A CLI utility to execute scripts from within markdown files.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tzador/makedown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    python_requires='>=3',
)
