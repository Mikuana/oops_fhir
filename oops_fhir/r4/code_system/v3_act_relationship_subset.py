from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActRelationshipSubset"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipSubset:
    """
    v3 Code System ActRelationshipSubset

     <ns1:p>Used to indicate that the target of the relationship will be a
filtered subset of the total related set of targets.</ns1:p><ns1:p>Used
when there is a need to limit the number of components to the first, the
last, the next, the total, the average or some other filtered or
calculated subset.</ns1:p>

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipSubset
    """

    underscore_participation_subset = CodeSystemConcept(
        {
            "code": "_ParticipationSubset",
            "concept": [
                {
                    "code": "FUTURE",
                    "concept": [
                        {
                            "code": "FUTSUM",
                            "definition": "Represents a 'summary' of all acts that are scheduled to occur in the future (whose effective time is greater than 'now' where is the time the instance is authored.). The effectiveTime represents the outer boundary of all occurrences, repeatNumber represents the total number of repetitions, etc.",
                            "display": "future summary",
                        },
                        {
                            "code": "LAST",
                            "definition": "Restricted to the latest known occurrence that is scheduled to occur. The Act with the highest known effective time.",
                            "display": "expected last",
                        },
                        {
                            "code": "NEXT",
                            "definition": "Restricted to the nearest recent known occurrence scheduled to occur in the future. The Act with the lowest effective time, still greater than 'now'. ('now' is the time the instance is authored.)",
                            "display": "expected next",
                        },
                    ],
                    "definition": "An occurrence that is scheduled to occur in the future. An Act whose effective time is greater than 'now', where 'now' is the time the instance is authored.",
                    "display": "expected future",
                },
                {
                    "code": "PAST",
                    "concept": [
                        {
                            "code": "FIRST",
                            "definition": "Restricted to the earliest known occurrence that occurred or was scheduled to occur in the past. The Act with the lowest effective time. ('now' is the time the instance is authored.)",
                            "display": "first known",
                        },
                        {
                            "code": "PREVSUM",
                            "definition": "Represents a 'summary' of all acts that previously occurred or were scheduled to occur. The effectiveTime represents the outer boundary of all occurrences, repeatNumber represents the total number of repetitions, etc. ('now' is the time the instance is authored.)",
                            "display": "previous summary",
                        },
                        {
                            "code": "RECENT",
                            "definition": "Restricted to the most recent known occurrence that occurred or was scheduled to occur in the past. The Act with the most recent effective time, still less than 'now'. ('now' is the time the instance is authored.)",
                            "display": "most recent",
                        },
                    ],
                    "definition": "An occurrence that occurred or was scheduled to occur in the past. An Act whose effective time is less than 'now'. ('now' is the time the instance is authored.)",
                    "display": "previous",
                },
                {
                    "code": "SUM",
                    "definition": "Represents a 'summary' of all acts that have occurred or were scheduled to occur and which are scheduled to occur in the future. The effectiveTime represents the outer boundary of all occurrences, repeatNumber represents the total number of repetitions, etc.",
                    "display": "summary",
                },
            ],
            "definition": "Used to indicate that the participation is a filtered subset of the total participations of the same type owned by the Act. \r\n\n                        Used when there is a need to limit the participations to the first, the last, the next or some other filtered subset.",
            "display": "ParticipationSubset",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ParticipationSubset

    Used to indicate that the participation is a filtered subset of the total participations of the same type owned by the Act. 

                        Used when there is a need to limit the participations to the first, the last, the next or some other filtered subset.
    """

    act_relationship_expected_subset = CodeSystemConcept(
        {
            "code": "ActRelationshipExpectedSubset",
            "definition": "ActRelationshipExpectedSubset",
            "display": "ActRelationshipExpectedSubset",
        }
    )
    """
    ActRelationshipExpectedSubset

    ActRelationshipExpectedSubset
    """

    act_relationship_past_subset = CodeSystemConcept(
        {
            "code": "ActRelationshipPastSubset",
            "definition": "ActRelationshipPastSubset",
            "display": "ActRelationshipPastSubset",
        }
    )
    """
    ActRelationshipPastSubset

    ActRelationshipPastSubset
    """

    max_ = CodeSystemConcept(
        {
            "code": "MAX",
            "definition": "The occurrence whose value attribute is greater than all other occurrences at the time the instance is created.",
            "display": "maximum",
        }
    )
    """
    maximum

    The occurrence whose value attribute is greater than all other occurrences at the time the instance is created.
    """

    min_ = CodeSystemConcept(
        {
            "code": "MIN",
            "definition": "The occurrence whose value attribute is less than all other occurrences at the time the instance is created.",
            "display": "minimum",
        }
    )
    """
    minimum

    The occurrence whose value attribute is less than all other occurrences at the time the instance is created.
    """

    class Meta:
        resource = _resource
