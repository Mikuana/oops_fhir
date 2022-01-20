from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DataAbsentReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DataAbsentReason:
    """
    DataAbsentReason

    Used to specify why the normally expected content of the data element is
missing.

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/data-absent-reason
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "concept": [
                {
                    "code": "asked-unknown",
                    "definition": "The source was asked but does not know the value.",
                    "display": "Asked But Unknown",
                },
                {
                    "code": "temp-unknown",
                    "definition": "There is reason to expect (from the workflow) that the value may become known.",
                    "display": "Temporarily Unknown",
                },
                {
                    "code": "not-asked",
                    "definition": "The workflow didn't lead to this value being known.",
                    "display": "Not Asked",
                },
                {
                    "code": "asked-declined",
                    "definition": "The source was asked but declined to answer.",
                    "display": "Asked But Declined",
                },
            ],
            "definition": "The value is expected to exist but is not known.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The value is expected to exist but is not known.
    """

    masked = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": 'Using "masked" may be breach of security or confidentiality, but there are times when its use is required to support alternate workflows for gaining access to denied information.',
                }
            ],
            "code": "masked",
            "definition": "The information is not available due to security, privacy or related reasons.",
            "display": "Masked",
        }
    )
    """
    Masked

    The information is not available due to security, privacy or related reasons.
    """

    not_applicable = CodeSystemConcept(
        {
            "code": "not-applicable",
            "definition": "There is no proper value for this element (e.g. last menstrual period for a male).",
            "display": "Not Applicable",
        }
    )
    """
    Not Applicable

    There is no proper value for this element (e.g. last menstrual period for a male).
    """

    unsupported = CodeSystemConcept(
        {
            "code": "unsupported",
            "definition": "The source system wasn't capable of supporting this element.",
            "display": "Unsupported",
        }
    )
    """
    Unsupported

    The source system wasn't capable of supporting this element.
    """

    as_text = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "It may be linked by internal references (e.g. xml:id). This usually implies that the value could not be represented in the correct format - this may be due to system limitations, or this particular data value.",
                }
            ],
            "code": "as-text",
            "definition": "The content of the data is represented in the resource narrative.",
            "display": "As Text",
        }
    )
    """
    As Text

    The content of the data is represented in the resource narrative.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "concept": [
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                            "valueString": "This is sometimes an output value from measuring devices.",
                        }
                    ],
                    "code": "not-a-number",
                    "definition": "The numeric value is undefined or unrepresentable due to a floating point processing error.",
                    "display": "Not a Number (NaN)",
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                            "valueString": "This is sometimes an output value from measuring devices.",
                        }
                    ],
                    "code": "negative-infinity",
                    "definition": "The numeric value is excessively low and unrepresentable due to a floating point processing error.",
                    "display": "Negative Infinity (NINF)",
                },
                {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                            "valueString": "This is sometimes an output value from measuring devices.",
                        }
                    ],
                    "code": "positive-infinity",
                    "definition": "The numeric value is excessively high and unrepresentable due to a floating point processing error.",
                    "display": "Positive Infinity (PINF)",
                },
            ],
            "definition": "Some system or workflow process error means that the information is not available.",
            "display": "Error",
        }
    )
    """
    Error

    Some system or workflow process error means that the information is not available.
    """

    not_performed = CodeSystemConcept(
        {
            "code": "not-performed",
            "definition": "The value is not available because the observation procedure (test, etc.) was not performed.",
            "display": "Not Performed",
        }
    )
    """
    Not Performed

    The value is not available because the observation procedure (test, etc.) was not performed.
    """

    not_permitted = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "This is most often associated with required bindings that do not include the actual code used, but may be used with other data types.",
                }
            ],
            "code": "not-permitted",
            "definition": "The value is not permitted in this context (e.g. due to profiles, or the base data types).",
            "display": "Not Permitted",
        }
    )
    """
    Not Permitted

    The value is not permitted in this context (e.g. due to profiles, or the base data types).
    """

    class Meta:
        resource = _resource
