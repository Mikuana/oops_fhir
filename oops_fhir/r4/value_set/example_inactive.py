from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet, CodeSystemConcept


__all__ = ["Exampleinactive"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Exampleinactive(ValueSet):
    """
    Example with inactive codes

    HL7 v3 ActMood Predicate codes, including inactive codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/inactive
    """

    # TODO: fix this template issue1
    pass

    crt = CodeSystemConcept(
        {
            "code": "CRT",
            "display": "criterion",
            "inactive": True,
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActMood",
        }
    )
    """ criterion """

    expec = CodeSystemConcept(
        {
            "code": "EXPEC",
            "contains": [
                {
                    "code": "GOL",
                    "display": "goal",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActMood",
                },
                {
                    "code": "RSK",
                    "display": "risk",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActMood",
                },
            ],
            "display": "expectation",
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActMood",
        }
    )
    """ expectation """

    opt = CodeSystemConcept(
        {
            "code": "OPT",
            "display": "option",
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActMood",
        }
    )
    """ option """

    class Meta:
        resource = _resource
