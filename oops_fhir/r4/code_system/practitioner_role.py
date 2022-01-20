from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PractitionerRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PractitionerRole:
    """
    Practitioner role

    This example value set defines a set of codes that can be used to
indicate the role of a Practitioner.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from SNOMED Clinical Terms® (SNOMED CT®) which is copyright of the International Health Terminology Standards Development Organisation (IHTSDO). Implementers of these specifications must have the appropriate SNOMED CT Affiliate license - for more information contact http://www.snomed.org/snomed-ct/get-snomed-ct or info@snomed.org

    http://terminology.hl7.org/CodeSystem/practitioner-role
    """

    doctor = CodeSystemConcept(
        {
            "code": "doctor",
            "definition": "A qualified/registered medical practitioner",
            "display": "Doctor",
        }
    )
    """
    Doctor

    A qualified/registered medical practitioner
    """

    nurse = CodeSystemConcept(
        {
            "code": "nurse",
            "definition": "A practitioner with nursing experience that may be qualified/registered",
            "display": "Nurse",
        }
    )
    """
    Nurse

    A practitioner with nursing experience that may be qualified/registered
    """

    pharmacist = CodeSystemConcept(
        {
            "code": "pharmacist",
            "definition": "A qualified/registered/licensed pharmacist",
            "display": "Pharmacist",
        }
    )
    """
    Pharmacist

    A qualified/registered/licensed pharmacist
    """

    researcher = CodeSystemConcept(
        {
            "code": "researcher",
            "definition": "A practitioner that may perform research",
            "display": "Researcher",
        }
    )
    """
    Researcher

    A practitioner that may perform research
    """

    teacher = CodeSystemConcept(
        {
            "code": "teacher",
            "definition": "Someone who is able to provide educational services",
            "display": "Teacher/educator",
        }
    )
    """
    Teacher/educator

    Someone who is able to provide educational services
    """

    ict = CodeSystemConcept(
        {
            "code": "ict",
            "definition": "Someone who is qualified in Information and Communication Technologies",
            "display": "ICT professional",
        }
    )
    """
    ICT professional

    Someone who is qualified in Information and Communication Technologies
    """

    class Meta:
        resource = _resource
