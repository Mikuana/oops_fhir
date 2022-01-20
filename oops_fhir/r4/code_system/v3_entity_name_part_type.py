from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNamePartType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartType:
    """
    v3 Code System EntityNamePartType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNamePartType
    """

    del_ = CodeSystemConcept(
        {
            "code": "DEL",
            "definition": "A delimiter has no meaning other than being literally printed in this name representation.  A delimiter has no implicit leading and trailing white space.",
            "display": "delimiter",
        }
    )
    """
    delimiter

    A delimiter has no meaning other than being literally printed in this name representation.  A delimiter has no implicit leading and trailing white space.
    """

    fam = CodeSystemConcept(
        {
            "code": "FAM",
            "definition": "Family name, this is the name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.",
            "display": "family",
        }
    )
    """
    family

    Family name, this is the name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.
    """

    giv = CodeSystemConcept(
        {
            "code": "GIV",
            "definition": 'Given name (don\'t call it "first name" since this given names do not always come first)',
            "display": "given",
        }
    )
    """
    given

    Given name (don't call it "first name" since this given names do not always come first)
    """

    pfx = CodeSystemConcept(
        {
            "code": "PFX",
            "definition": "A prefix has a strong association to the immediately following name part. A prefix has no implicit trailing white space (it has implicit leading white space though). Note that prefixes can be inverted.",
            "display": "prefix",
        }
    )
    """
    prefix

    A prefix has a strong association to the immediately following name part. A prefix has no implicit trailing white space (it has implicit leading white space though). Note that prefixes can be inverted.
    """

    sfx = CodeSystemConcept(
        {
            "code": "SFX",
            "definition": "Description:A suffix has a strong association to the immediately preceding name part. A suffix has no implicit leading white space (it has implicit trailing white space though). Suffices cannot be inverted.",
            "display": "suffix",
        }
    )
    """
    suffix

    Description:A suffix has a strong association to the immediately preceding name part. A suffix has no implicit leading white space (it has implicit trailing white space though). Suffices cannot be inverted.
    """

    class Meta:
        resource = _resource
