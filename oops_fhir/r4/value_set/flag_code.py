from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["FlagCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FlagCode(SNOMEDCT):
    """
    Flag Code

    Example list of detail codes for flagged issues.  (Not complete or
necessarily appropriate.)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/flag-code
    """

    class Meta:
        resource = _resource
