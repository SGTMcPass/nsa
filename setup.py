#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""NASA Simulation Agents - Setup configuration.

This module configures the package metadata and dependencies for the NASA Simulation Agents project.
"""

import os
import re
from pathlib import Path

from setuptools import find_packages, setup

# Read requirements from requirements.in
with open("requirements.in", encoding="utf-8") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith(("#", "-r", "--"))
    ]

# Read development requirements
with open("requirements-dev.in", encoding="utf-8") as f:
    dev_requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith(("#", "-r", "--"))
    ]

def get_version() -> str:
    """Get the package version from __init__.py.

    Returns:
        str: The package version.
    """
    version_file = os.path.join("tools", "__init__.py")
    if not os.path.exists(version_file):
        with open(version_file, "w", encoding="utf-8") as f:
            f.write('__version__ = "0.1.0"\n')
    
    with open(version_file, "r", encoding="utf-8") as f:
        version_match = re.search(
            r'^__version__ = ["\']([^"\']*)["\']', f.read(), re.M
        )
    
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read_readme() -> str:
    """Read the README.md file.

    Returns:
        str: The content of the README.md file.
    """
    try:
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "NASA Simulation Agents - AI-powered simulation tools for space mission planning and analysis"


setup(
    name="nasa-simulation-agents",
    version=get_version(),
    description=(
        "AI-powered simulation tools for space mission planning and analysis"
    ),
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="NASA Simulation Team",
    author_email="simulation@nasa.example.com",
    url="https://github.com/your-org/nasa-simulation-agents",
    packages=find_packages(where="tools"),
    package_dir={"": "tools"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "docs": [
            "sphinx>=7.2.6",
            "sphinx-rtd-theme>=2.0.0",
            "myst-parser>=2.0.0",
            "sphinx-autodoc-typehints>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "chunker=chunker_lib.cli:main",
            "embedder=embedding_lib.embedding_cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=(
        "nasa simulation ai machine-learning space-mission planning analysis"
    ),
    project_urls={
        "Bug Reports": "https://github.com/your-org/nasa-simulation-agents/issues",
        "Source": "https://github.com/your-org/nasa-simulation-agents",
    },
    license="Apache 2.0",
)
