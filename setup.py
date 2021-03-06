#!/usr/bin/env python

"""The setup script."""

import re
from pathlib import Path

from setuptools import setup, find_packages

readme = Path("README.md").read_text()


def read_version():
    try:
        v = [
            x
            for x in Path("oops_fhir/__init__.py").open()
            if x.startswith("__version__")
        ][0]
        v = re.match(r"__version__ *= *'(.*?)'\n", v)[1]
        return v
    except Exception as e:
        raise RuntimeError(f"Unable to read version string: {e}")


requirements = [
    "fhir.resources"
]

test_requirements = [
    "pytest>=3",
    'pytest-cov'
]

setup(
    author="Christopher Boyd",
    author_email="mikuana@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Object-Oriented Programming Support for Fast Healthcare Interopere Resources (FHIR)",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n",
    include_package_data=True,
    keywords="oops_fhir",
    name="oops_fhir",
    packages=find_packages(include=["oops_fhir", "oops_fhir.*"]),
    extras_require={
        'Testing': [test_requirements]
    },
    url="https://github.com/mikuana/oops_fhir",
    version="0.1.0-beta",
    zip_safe=False,
)
