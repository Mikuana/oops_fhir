from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet, CodeSystemConcept


__all__ = ["YesNoDontKnow"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class YesNoDontKnow(ValueSet):
    """
    Yes/No/Don't Know

    For Capturing simple yes-no-don't know answers

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/yesnodontknow
    """

    # TODO: fix this template issue1
    pass

    y = CodeSystemConcept(
        {
            "code": "Y",
            "display": "Yes",
            "system": "http://terminology.hl7.org/CodeSystem/v2-0136",
        }
    )
    """ Yes """

    n = CodeSystemConcept(
        {
            "code": "N",
            "display": "No",
            "system": "http://terminology.hl7.org/CodeSystem/v2-0136",
        }
    )
    """ No """

    asked_unknown = CodeSystemConcept(
        {
            "code": "asked-unknown",
            "display": "Don't know",
            "system": "http://terminology.hl7.org/CodeSystem/data-absent-reason",
        }
    )
    """ Don't know """

    class Meta:
        resource = _resource
