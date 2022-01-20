from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NameUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NameUse:
    """
    NameUse

    The use of a human name.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/name-use
    """

    usual = CodeSystemConcept(
        {
            "code": "usual",
            "definition": "Known as/conventional/the one you normally use.",
            "display": "Usual",
        }
    )
    """
    Usual

    Known as/conventional/the one you normally use.
    """

    official = CodeSystemConcept(
        {
            "code": "official",
            "definition": 'The formal name as registered in an official (government) registry, but which name might not be commonly used. May be called "legal name".',
            "display": "Official",
        }
    )
    """
    Official

    The formal name as registered in an official (government) registry, but which name might not be commonly used. May be called "legal name".
    """

    temp = CodeSystemConcept(
        {
            "code": "temp",
            "definition": "A temporary name. Name.period can provide more detailed information. This may also be used for temporary names assigned at birth or in emergency situations.",
            "display": "Temp",
        }
    )
    """
    Temp

    A temporary name. Name.period can provide more detailed information. This may also be used for temporary names assigned at birth or in emergency situations.
    """

    nickname = CodeSystemConcept(
        {
            "code": "nickname",
            "definition": "A name that is used to address the person in an informal manner, but is not part of their formal or usual name.",
            "display": "Nickname",
        }
    )
    """
    Nickname

    A name that is used to address the person in an informal manner, but is not part of their formal or usual name.
    """

    anonymous = CodeSystemConcept(
        {
            "code": "anonymous",
            "definition": "Anonymous assigned name, alias, or pseudonym (used to protect a person's identity for privacy reasons).",
            "display": "Anonymous",
        }
    )
    """
    Anonymous

    Anonymous assigned name, alias, or pseudonym (used to protect a person's identity for privacy reasons).
    """

    old = CodeSystemConcept(
        {
            "code": "old",
            "concept": [
                {
                    "code": "maiden",
                    "definition": "A name used prior to changing name because of marriage. This name use is for use by applications that collect and store names that were used prior to a marriage. Marriage naming customs vary greatly around the world, and are constantly changing. This term is not gender specific. The use of this term does not imply any particular history for a person's name.",
                    "display": "Name changed for Marriage",
                }
            ],
            "definition": "This name is no longer in use (or was never correct, but retained for records).",
            "display": "Old",
        }
    )
    """
    Old

    This name is no longer in use (or was never correct, but retained for records).
    """

    class Meta:
        resource = _resource
