from setuptools import setup
import makedown

setup(
    name="makedown",
    version=makedown.version,
    py_modules=['makedown'],
    entry_points={
        'console_scripts': [
            'makedown=makedown:main',
            'm=makedown:main',
        ],
    },
    install_requires=[
        # List of dependencies
    ],
    author="Tim Zadorozhny",
    author_email="tzador@gmail.com",
    description="A Markdown-based Makefile alternative.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tzador/makedown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    python_requires='>=3',
    license_files=('LICENSE',),
)
