from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.diagnosis_role import DiagnosisRole as DiagnosisRole_


__all__ = ["DiagnosisRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosisRole(DiagnosisRole_):
    """
    DiagnosisRole

    This value set defines a set of codes that can be used to express the
role of a diagnosis on the Encounter or EpisodeOfCare record.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/diagnosis-role
    """

    class Meta:
        resource = _resource
