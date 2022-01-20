from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.use import Use as Use_


__all__ = ["Use"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Use(Use_):
    """
    Use

    The purpose of the Claim: predetermination, preauthorization, claim.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-use
    """

    class Meta:
        resource = _resource
