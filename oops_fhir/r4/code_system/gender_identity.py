from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GenderIdentity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GenderIdentity:
    """
    Gender identity

    This example value set defines a set of codes that can be used to
indicate a patient's gender identity.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from SNOMED Clinical Terms® (SNOMED CT®) which is copyright of the International Health Terminology Standards Development Organisation (IHTSDO). Implementers of these specifications must have the appropriate SNOMED CT Affiliate license - for more information contact http://www.snomed.org/snomed-ct/get-snomed-ct or info@snomed.org

    http://hl7.org/fhir/gender-identity
    """

    transgender_female = CodeSystemConcept(
        {
            "code": "transgender-female",
            "definition": "the patient identifies as transgender male-to-female",
            "display": "transgender female",
        }
    )
    """
    transgender female

    the patient identifies as transgender male-to-female
    """

    transgender_male = CodeSystemConcept(
        {
            "code": "transgender-male",
            "definition": "the patient identifies as transgender female-to-male",
            "display": "transgender male",
        }
    )
    """
    transgender male

    the patient identifies as transgender female-to-male
    """

    non_binary = CodeSystemConcept(
        {
            "code": "non-binary",
            "definition": "the patient identifies with neither/both female and male",
            "display": "non-binary",
        }
    )
    """
    non-binary

    the patient identifies with neither/both female and male
    """

    male = CodeSystemConcept(
        {
            "code": "male",
            "definition": "the patient identifies as male",
            "display": "male",
        }
    )
    """
    male

    the patient identifies as male
    """

    female = CodeSystemConcept(
        {
            "code": "female",
            "definition": "the patient identifies as female",
            "display": "female",
        }
    )
    """
    female

    the patient identifies as female
    """

    other = CodeSystemConcept(
        {"code": "other", "definition": "other gender identity", "display": "other"}
    )
    """
    other

    other gender identity
    """

    non_disclose = CodeSystemConcept(
        {
            "code": "non-disclose",
            "definition": "the patient does not wish to disclose his gender identity",
            "display": "does not wish to disclose",
        }
    )
    """
    does not wish to disclose

    the patient does not wish to disclose his gender identity
    """

    class Meta:
        resource = _resource
