from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["BodyLengthUnits"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BodyLengthUnits(ValueSet):
    """
    Body Length Units

    UCUM units for recording body length measures such as height and head
circumference

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ucum-bodylength
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
