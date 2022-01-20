from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNameUseR2"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNameUseR2:
    """
    v3 Code System EntityNameUseR2

      Description:  A set of codes advising a system or user which name in a
set of names to select for a given purpose.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNameUseR2
    """

    assumed = CodeSystemConcept(
        {
            "code": "Assumed",
            "concept": [
                {
                    "code": "A",
                    "definition": "Description:A name used in a Professional or Business context .  Examples: Continuing to use a maiden name in a professional context, or using a stage performing name (some of these names are also pseudonyms)",
                    "display": "business name",
                },
                {
                    "code": "ANON",
                    "definition": "Description:Anonymous assigned name (used to protect a persons identity for privacy reasons)",
                    "display": "Anonymous",
                },
                {
                    "code": "I",
                    "definition": "Description:e.g .  Chief Red Cloud",
                    "display": "Indigenous/Tribal",
                },
                {
                    "code": "P",
                    "definition": "Description:A non-official name by which the person is sometimes known.  (This may also be used to record informal names such as a nickname)",
                    "display": "Other/Pseudonym/Alias",
                },
                {
                    "code": "R",
                    "definition": "Description:A name assumed as part of a religious vocation .  e.g .  Sister Mary Francis, Brother John",
                    "display": "religious",
                },
            ],
            "definition": "Description:A name that a person has assumed or has been assumed to them.",
            "display": "Assumed",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Assumed

    Description:A name that a person has assumed or has been assumed to them.
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Description:Known as/conventional/the one you normally use",
            "display": "customary",
        }
    )
    """
    customary

    Description:Known as/conventional/the one you normally use
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "Description:A name used prior to marriage.Note that marriage naming customs vary greatly around the world.  This name use is for use by applications that collect and store maiden names.  Though the concept of maiden name is often gender specific, the use of this term is not gender specific.  The use of this term does not imply any particular history for a person's name, nor should the maiden name be determined algorithmically",
            "display": "maiden name",
        }
    )
    """
    maiden name

    Description:A name used prior to marriage.Note that marriage naming customs vary greatly around the world.  This name use is for use by applications that collect and store maiden names.  Though the concept of maiden name is often gender specific, the use of this term is not gender specific.  The use of this term does not imply any particular history for a person's name, nor should the maiden name be determined algorithmically
    """

    name_representation_use = CodeSystemConcept(
        {
            "code": "NameRepresentationUse",
            "concept": [
                {
                    "code": "ABC",
                    "definition": "Description:Alphabetic transcription of name in latin alphabet (Japanese: romaji)",
                    "display": "alphabetic",
                },
                {
                    "code": "IDE",
                    "definition": "Description:Ideographic representation of name (e.g., Japanese kanji, Chinese characters)",
                    "display": "ideographic",
                },
                {
                    "code": "SYL",
                    "definition": "Description:Syllabic transcription of name (e.g., Japanese kana, Korean hangul)",
                    "display": "syllabic",
                },
            ],
            "definition": "Description:Identifies the different representations of a name .  The representation may affect how the name is used .  (E.g .  use of Ideographic for formal communications.)",
            "display": "NameRepresentationUse",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    NameRepresentationUse

    Description:Identifies the different representations of a name .  The representation may affect how the name is used .  (E.g .  use of Ideographic for formal communications.)
    """

    old = CodeSystemConcept(
        {
            "code": "OLD",
            "concept": [
                {
                    "code": "DN",
                    "definition": 'Description:This name should no longer be used when interacting with the person (i.e .  in addition to no longer being used, the name should not be even mentioned when interacting with the person)Note: applications are not required to compare names labeled "Do Not Use" and other names in order to eliminate name parts that are common between the other name and a name labeled "Do Not Use".',
                    "display": "do not use",
                }
            ],
            "definition": "Description:This name is no longer in use (note: Names may also carry valid time ranges .  This code is used to cover the situations where it is known that the name is no longer valid, but no particular time range for its use is known)",
            "display": "no longer in use",
        }
    )
    """
    no longer in use

    Description:This name is no longer in use (note: Names may also carry valid time ranges .  This code is used to cover the situations where it is known that the name is no longer valid, but no particular time range for its use is known)
    """

    or_ = CodeSystemConcept(
        {
            "code": "OR",
            "definition": "Description:The formal name as registered in an official (government) registry, but which name might not be commonly used .  May correspond to the concept of legal name",
            "display": "official registry name",
        }
    )
    """
    official registry name

    Description:The formal name as registered in an official (government) registry, but which name might not be commonly used .  May correspond to the concept of legal name
    """

    phon = CodeSystemConcept(
        {
            "code": "PHON",
            "definition": "Description:The name as understood by the data enterer, i.e. a close approximation of a phonetic spelling of the name, not based on a phonetic algorithm.",
            "display": "phonetic",
        }
    )
    """
    phonetic

    Description:The name as understood by the data enterer, i.e. a close approximation of a phonetic spelling of the name, not based on a phonetic algorithm.
    """

    srch = CodeSystemConcept(
        {
            "code": "SRCH",
            "definition": "Description:A name intended for use in searching or matching.  This is used when the name is incomplete and contains enough details for search matching, but not enough for other uses.",
            "display": "search",
        }
    )
    """
    search

    Description:A name intended for use in searching or matching.  This is used when the name is incomplete and contains enough details for search matching, but not enough for other uses.
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Description:A temporary name.  Note that a name valid time can provide more detailed information.  This may also be used for temporary names assigned at birth or in emergency situations.",
            "display": "temporary",
        }
    )
    """
    temporary

    Description:A temporary name.  Note that a name valid time can provide more detailed information.  This may also be used for temporary names assigned at birth or in emergency situations.
    """

    class Meta:
        resource = _resource
