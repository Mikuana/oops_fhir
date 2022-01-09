"""
AbstractType

A list of the base types defined by this version of the FHIR
specification - types that are defined, but for which only
specializations actually are created.

Status: active - Version: 4.0.1

http://hl7.org/fhir/abstract-types
"""
from pathlib import Path

from fhir.resources.codesystem import CodeSystem


__all__ = [
    "v_type",
    "v_any",
]


v_type = {
    "code": "Type",
    "definition": "A place holder that means any kind of data type",
    "display": "Type",
}
""" A place holder that means any kind of data type """

v_any = {
    "code": "Any",
    "definition": "A place holder that means any kind of resource",
    "display": "Any",
}
""" A place holder that means any kind of resource """


resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))
