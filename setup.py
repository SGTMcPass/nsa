from setuptools import setup, find_packages

setup(
    name="trick_chunker",
    version="0.1.0",
    description="CLI tool to chunk Trick documentation into vector-ready pieces",
    author="Your Name",
    packages=find_packages(where="tools"),
    package_dir={"": "tools"},
    install_requires=[
        "PyYAML",
        "markdown-it-py",
        "tiktoken",
    ],
    entry_points={
        "console_scripts": [
            "chunker=chunker_lib.cli:main",
        ],
    },
)
