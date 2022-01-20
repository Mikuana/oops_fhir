from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PractitionerSpecialty"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PractitionerSpecialty:
    """
    Practitioner specialty

    This example value set defines a set of codes that can be used to
indicate the specialty of a Practitioner.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/practitioner-specialty
    """

    cardio = CodeSystemConcept({"code": "cardio", "display": "Cardiologist"})
    """
    Cardiologist

    
    """

    dent = CodeSystemConcept({"code": "dent", "display": "Dentist"})
    """
    Dentist

    
    """

    dietary = CodeSystemConcept({"code": "dietary", "display": "Dietary consultant"})
    """
    Dietary consultant

    
    """

    midw = CodeSystemConcept({"code": "midw", "display": "Midwife"})
    """
    Midwife

    
    """

    sysarch = CodeSystemConcept({"code": "sysarch", "display": "Systems architect"})
    """
    Systems architect

    
    """

    class Meta:
        resource = _resource
