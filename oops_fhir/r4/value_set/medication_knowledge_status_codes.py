from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_knowledge_status_codes import (
    MedicationKnowledgeStatusCodes as MedicationKnowledgeStatusCodes_,
)


__all__ = ["MedicationKnowledgeStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationKnowledgeStatusCodes(MedicationKnowledgeStatusCodes_):
    """
    Medication knowledge  status  codes

    MedicationKnowledge Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationknowledge-status
    """

    class Meta:
        resource = _resource
