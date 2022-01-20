from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNamePartTypeR2"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartTypeR2:
    """
    v3 Code System EntityNamePartTypeR2

      Description:  Indicates whether the name part is a given name, family
name, prefix, suffix, etc.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNamePartTypeR2
    """

    del_ = CodeSystemConcept(
        {
            "code": "DEL",
            "definition": "Description:A delimiter has no meaning other than being literally printed in this name representation. A delimiter has no implicit leading and trailing white space.",
            "display": "delimiter",
        }
    )
    """
    delimiter

    Description:A delimiter has no meaning other than being literally printed in this name representation. A delimiter has no implicit leading and trailing white space.
    """

    fam = CodeSystemConcept(
        {
            "code": "FAM",
            "definition": "Description:Family name, this is the name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.",
            "display": "family",
        }
    )
    """
    family

    Description:Family name, this is the name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.
    """

    giv = CodeSystemConcept(
        {
            "code": "GIV",
            "definition": 'Description:Given name. Note: don\'t call it "first name" since the given names do not always come first.',
            "display": "given",
        }
    )
    """
    given

    Description:Given name. Note: don't call it "first name" since the given names do not always come first.
    """

    title = CodeSystemConcept(
        {
            "code": "TITLE",
            "definition": "Description:Part of the name that is acquired as a title due to academic, legal, employment or nobility status etc.\r\n\n                        \n                           Note:Title name parts include name parts that come after the name such as qualifications, even if they are not always considered to be titles.",
            "display": "title",
        }
    )
    """
    title

    Description:Part of the name that is acquired as a title due to academic, legal, employment or nobility status etc.

                        
                           Note:Title name parts include name parts that come after the name such as qualifications, even if they are not always considered to be titles.
    """

    class Meta:
        resource = _resource
