# OOPS FHIR

[![PyPI](https://img.shields.io/pypi/v/oops_fhir)](https://pypi.org/project/oops_fhir/)
[![Documentation Status](https://readthedocs.org/projects/oops_fhir/badge/)](https://oops_fhir.readthedocs.io/)
[![CodeStyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/github/license/mikuana/oops_fhir)

Object-Oriented Programming Support for Fast Healthcare Interoperable Resources.

> **WARNING**:
> This project is still in a beta state, and is subject to sudden, violent
> changes to the code base. You have been warned.

This package seeks to make the use of FHIR objects in a Python IDE more
accessible and interactive. Although public repositories of FHIR artifacts
exist, they do not integrate into Python IDEs in a way that allows for the use
of quick-documentation, type hinting, or dot-notation to access attributes or
enumerated values.

This package does not intend to add anything *new* to the FHIR artifacts that
exist, nor does it attempt to replace packages like
[fhir.resources](https://pypi.org/project/fhir.resources/).
Rather, it seeks to expose helpful information about these artifacts in ways
that can be accessed by an IDE, to assist in the work of converting non-FHIR
data into FHIR format.
