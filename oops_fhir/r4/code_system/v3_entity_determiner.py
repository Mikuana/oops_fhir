from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityDeterminer"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityDeterminer:
    """
    v3 Code System EntityDeterminer

     EntityDeterminer in natural language grammar is the class of words that
comprises articles, demonstrative pronouns, and quantifiers. In the RIM,
determiner is a structural code in the Entity class to distinguish
whether any given Entity object stands for some, any one, or a specific
thing.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityDeterminer
    """

    instance = CodeSystemConcept(
        {
            "code": "INSTANCE",
            "concept": [
                {
                    "code": "GROUP",
                    "definition": "A determiner that specifies that the Entity object represents a particular collection of physical things (as opposed to a universal, kind, or class of physical thing).  While the collection may resolve to having only a single individual (or even no individuals), the potential should exist for it to cover multiple individuals.",
                    "display": "specific group",
                }
            ],
            "definition": "Description:A determiner that specifies that the Entity object represents a particular physical thing (as opposed to a universal, kind, or class of physical thing).\r\n\n                        \n                           Discussion: It does not matter whether an INSTANCE still exists as a whole at the point in time (or process) when we mention it, for example, a drug product lot is an INSTANCE even though it has been portioned out for retail purpose.",
            "display": "specific",
        }
    )
    """
    specific

    Description:A determiner that specifies that the Entity object represents a particular physical thing (as opposed to a universal, kind, or class of physical thing).

                        
                           Discussion: It does not matter whether an INSTANCE still exists as a whole at the point in time (or process) when we mention it, for example, a drug product lot is an INSTANCE even though it has been portioned out for retail purpose.
    """

    kind = CodeSystemConcept(
        {
            "code": "KIND",
            "concept": [
                {
                    "code": "GROUPKIND",
                    "definition": "A determiner that specifies that the Entity object represents a universal, kind or class of collections physical things.  While the collection may resolve to having only a single individual (or even no individuals), the potential should exist for it to cover multiple individuals.",
                    "display": "described group",
                },
                {
                    "code": "QUANTIFIED_KIND",
                    "definition": "The described quantified determiner indicates that the given Entity is taken as a general description of a specific amount of a thing. For example, QUANTIFIED_KIND of syringe (quantity = 3,) stands for exactly three syringes.",
                    "display": "described quantified",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2008-11-14"},
                    ],
                },
            ],
            "definition": "Description:A determiner that specifies that the Entity object represents a universal, kind or class of physical thing (as opposed to a particular thing).",
            "display": "described",
        }
    )
    """
    described

    Description:A determiner that specifies that the Entity object represents a universal, kind or class of physical thing (as opposed to a particular thing).
    """

    class Meta:
        resource = _resource
