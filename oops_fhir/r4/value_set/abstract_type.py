"""
AbstractType

A list of the base types defined by this version of the FHIR specification - types that are defined, but for which only specializations actually are created.

http://hl7.org/fhir/ValueSet/abstract-types
"""

from pathlib import Path

from fhir.resources.valueset import ValueSet

# TODO: import referenced resources

resource = ValueSet.parse_file(Path(__file__).with_suffix(".json"))
