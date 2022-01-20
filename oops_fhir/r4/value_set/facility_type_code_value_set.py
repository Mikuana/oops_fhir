from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FacilityTypeCodeValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FacilityTypeCodeValueSet(ValueSet):
    """
    Facility Type Code Value Set

    This is the code representing the type of organizational setting where
the clinical encounter, service, interaction, or treatment occurred. The
value set used for Healthcare Facility Type has been defined by HITSP to
be the value set reproduced from HITSP C80 Table 2-147.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/c80-facilitycodes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
