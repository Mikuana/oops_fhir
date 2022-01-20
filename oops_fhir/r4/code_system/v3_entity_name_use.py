from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNameUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNameUse:
    """
    v3 Code System EntityNameUse

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNameUse
    """

    underscore_name_representation_use = CodeSystemConcept(
        {
            "code": "_NameRepresentationUse",
            "concept": [
                {
                    "code": "ABC",
                    "definition": "Alphabetic transcription of name (Japanese: romaji)",
                    "display": "Alphabetic",
                },
                {
                    "code": "IDE",
                    "definition": "Ideographic representation of name (e.g., Japanese kanji, Chinese characters)",
                    "display": "Ideographic",
                },
                {
                    "code": "SYL",
                    "definition": "Syllabic transcription of name (e.g., Japanese kana, Korean hangul)",
                    "display": "Syllabic",
                },
            ],
            "definition": "Identifies the different representations of a name.  The representation may affect how the name is used.  (E.g. use of Ideographic for formal communications.)",
            "display": "NameRepresentationUse",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    NameRepresentationUse

    Identifies the different representations of a name.  The representation may affect how the name is used.  (E.g. use of Ideographic for formal communications.)
    """

    asgn = CodeSystemConcept(
        {
            "code": "ASGN",
            "definition": 'A name assigned to a person. Reasons some organizations assign alternate names may include not knowing the person\'s name, or to maintain anonymity. Some, but not necessarily all, of the name types that people call "alias" may fit into this category.',
            "display": "assigned",
        }
    )
    """
    assigned

    A name assigned to a person. Reasons some organizations assign alternate names may include not knowing the person's name, or to maintain anonymity. Some, but not necessarily all, of the name types that people call "alias" may fit into this category.
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "As recorded on a license, record, certificate, etc. (only if different from legal name)",
            "display": "License",
        }
    )
    """
    License

    As recorded on a license, record, certificate, etc. (only if different from legal name)
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "e.g. Chief Red Cloud",
            "display": "Indigenous/Tribal",
        }
    )
    """
    Indigenous/Tribal

    e.g. Chief Red Cloud
    """

    l = CodeSystemConcept(
        {
            "code": "L",
            "concept": [
                {
                    "code": "OR",
                    "definition": "Definition:The formal name as registered in an official (government) registry, but which name might not be commonly used. Particularly used in countries with a law system based on Napoleonic law.",
                    "display": "official registry",
                }
            ],
            "definition": "Known as/conventional/the one you use",
            "display": "Legal",
        }
    )
    """
    Legal

    Known as/conventional/the one you use
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "concept": [
                {
                    "code": "A",
                    "definition": "Includes writer's pseudonym, stage name, etc",
                    "display": "Artist/Stage",
                }
            ],
            "definition": "A self asserted name that the person is using or has used.",
            "display": "pseudonym",
        }
    )
    """
    pseudonym

    A self asserted name that the person is using or has used.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "e.g. Sister Mary Francis, Brother John",
            "display": "Religious",
        }
    )
    """
    Religious

    e.g. Sister Mary Francis, Brother John
    """

    srch = CodeSystemConcept(
        {
            "code": "SRCH",
            "concept": [
                {
                    "code": "PHON",
                    "definition": "A name spelled phonetically.\r\n\n                        There are a variety of phonetic spelling algorithms. This code value does not distinguish between these.Discussion:",
                    "display": "phonetic",
                },
                {
                    "code": "SNDX",
                    "definition": "A name spelled according to the SoundEx algorithm.",
                    "display": "Soundex",
                },
            ],
            "definition": "A name intended for use in searching or matching.",
            "display": "search",
        }
    )
    """
    search

    A name intended for use in searching or matching.
    """

    class Meta:
        resource = _resource
