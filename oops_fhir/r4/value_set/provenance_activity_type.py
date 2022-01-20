from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["ProvenanceActivityType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceActivityType(ValueSet):
    """
    Provenance activity type

    This value set contains representative Activity Type codes, which
includes codes from the HL7 DocumentCompletion, ActStatus, and
DataOperations code system, W3C PROV-DM and PROV-N concepts and display
names, several HL7 Lifecycle Event codes for which there are agreed upon
definitions, and non-duplicated codes from the HL7 Security and Privacy
Ontology Operations codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/provenance-activity-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
