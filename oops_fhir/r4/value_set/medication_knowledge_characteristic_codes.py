from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_knowledge_characteristic_codes import (
    medicationKnowledgeCharacteristicCodes as medicationKnowledgeCharacteristicCodes_,
)


__all__ = ["medicationKnowledgeCharacteristicCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationKnowledgeCharacteristicCodes(medicationKnowledgeCharacteristicCodes_):
    """
    Medication knowledge  characteristic  codes

    MedicationKnowledge Characteristic Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationknowledge-characteristic
    """

    class Meta:
        resource = _resource
