=========
OOPS FHIR
=========


.. image:: https://img.shields.io/pypi/v/oops_fhir.svg
        :target: https://pypi.python.org/pypi/oops_fhir

.. image:: https://readthedocs.org/projects/oops-fhir/badge/?version=latest
        :target: https://oops-fhir.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


Object-Oriented Programming Support for Fast Healthcare Interoperable Resources.

.. warning::

    This project is still in a beta state, and is subject to sudden, violent
    changes to the code base. You have been warned.

This package seeks to make the use of FHIR objects in a Python IDE more
accessible and interactive. Although public repositories of FHIR artifacts
exist, they do not integrate into Python IDEs in a way that allows for the use
of quick-documentation, type hinting, or dot-notation to access attributes or
enumerated values.

This package does not intend to add anything *new* to the FHIR artifacts that
exist, nor does it attempt to replace packages like fhir.resources_. Rather, it
seeks to expose helpful information about these artifacts in ways that can be
accessed by an IDE, to assist in the work of converting non-FHIR data into
FHIR format.

* Free software: MIT license
* Documentation: https://oops-fhir.readthedocs.io.


Features
--------

* Code System Factory
* Value System Reference Resolver
* Bundle Resource Parser


ToDo
--------

- oops_fhir/r4/code_system/quantity_comparator.py GreaterThanEqual broken
- Link data type


.. _fhir.resources: https://pypi.org/project/fhir.resources/
