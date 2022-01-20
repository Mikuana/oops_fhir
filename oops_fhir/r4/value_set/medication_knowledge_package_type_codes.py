from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_knowledge_package_type_codes import (
    medicationKnowledgePackageTypeCodes as medicationKnowledgePackageTypeCodes_,
)


__all__ = ["medicationKnowledgePackageTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationKnowledgePackageTypeCodes(medicationKnowledgePackageTypeCodes_):
    """
    Medication knowledge  package  type  codes

    MedicationKnowledge Package Type Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationknowledge-package-type
    """

    class Meta:
        resource = _resource
