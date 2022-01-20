from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.need import need as need_


__all__ = ["need"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class need(need_):
    """
    Need

    The frequency with which the target must be validated

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-need
    """

    class Meta:
        resource = _resource
