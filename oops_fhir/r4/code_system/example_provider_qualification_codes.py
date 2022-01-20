from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleProviderQualificationCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProviderQualificationCodes:
    """
    Example Provider Qualification Codes

    This value set includes sample Provider Qualification codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-providerqualification
    """

    three11405 = CodeSystemConcept(
        {
            "code": "311405",
            "definition": "Dentist General Practitioner (DDS, DDM).",
            "display": "Dentist",
        }
    )
    """
    Dentist

    Dentist General Practitioner (DDS, DDM).
    """

    six04215 = CodeSystemConcept(
        {
            "code": "604215",
            "definition": "Ophthalmologist.",
            "display": "Ophthalmologist",
        }
    )
    """
    Ophthalmologist

    Ophthalmologist.
    """

    six04210 = CodeSystemConcept(
        {"code": "604210", "definition": "Optometrist.", "display": "Optometrist"}
    )
    """
    Optometrist

    Optometrist.
    """

    class Meta:
        resource = _resource
