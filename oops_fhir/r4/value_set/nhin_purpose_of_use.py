from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.nhin_purpose_of_use import (
    NHINPurposeOfUse as NHINPurposeOfUse_,
)


__all__ = ["NHINPurposeOfUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NHINPurposeOfUse(NHINPurposeOfUse_):
    """
    NHIN PurposeOfUse

    This value set is suitable for use with the provenance resource. It is
derived from, but not compatible with, the HL7 v3 Purpose of use Code
system.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/nhin-purposeofuse
    """

    class Meta:
        resource = _resource
