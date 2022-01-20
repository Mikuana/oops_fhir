from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.admit_source import AdmitSource as AdmitSource_


__all__ = ["AdmitSource"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdmitSource(AdmitSource_):
    """
    Admit source

    This value set defines a set of codes that can be used to indicate from
where the patient came in.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-admit-source
    """

    class Meta:
        resource = _resource
