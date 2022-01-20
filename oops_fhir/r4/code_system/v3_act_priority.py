from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActPriority"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActPriority:
    """
    v3 Code System ActPriority

     A set of codes (e.g., for routine, emergency), specifying the urgency
under which the Act happened, can happen, is happening, is intended to
happen, or is requested/demanded to happen.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActPriority
    """

    a = CodeSystemConcept(
        {
            "code": "A",
            "definition": "As soon as possible, next highest priority after stat.",
            "display": "ASAP",
        }
    )
    """
    ASAP

    As soon as possible, next highest priority after stat.
    """

    cr = CodeSystemConcept(
        {
            "code": "CR",
            "definition": 'Filler should contact the placer as soon as results are available, even for preliminary results.  (Was "C" in HL7 version 2.3\'s reporting priority.)',
            "display": "callback results",
        }
    )
    """
    callback results

    Filler should contact the placer as soon as results are available, even for preliminary results.  (Was "C" in HL7 version 2.3's reporting priority.)
    """

    cs = CodeSystemConcept(
        {
            "code": "CS",
            "concept": [
                {
                    "code": "CSP",
                    "definition": 'Filler should contact the placer to schedule the service.  (Was "C" in HL7 version 2.3\'s TQ-priority component.)',
                    "display": "callback placer for scheduling",
                },
                {
                    "code": "CSR",
                    "definition": 'Filler should contact the service recipient (target) to schedule the service.  (Was "C" in HL7 version 2.3\'s TQ-priority component.)',
                    "display": "contact recipient for scheduling",
                },
            ],
            "definition": 'Filler should contact the placer (or target) to schedule the service.  (Was "C" in HL7 version 2.3\'s TQ-priority component.)',
            "display": "callback for scheduling",
        }
    )
    """
    callback for scheduling

    Filler should contact the placer (or target) to schedule the service.  (Was "C" in HL7 version 2.3's TQ-priority component.)
    """

    el = CodeSystemConcept(
        {
            "code": "EL",
            "definition": "Beneficial to the patient but not essential for survival.",
            "display": "elective",
        }
    )
    """
    elective

    Beneficial to the patient but not essential for survival.
    """

    em = CodeSystemConcept(
        {
            "code": "EM",
            "definition": "An unforeseen combination of circumstances or the resulting state that calls for immediate action.",
            "display": "emergency",
        }
    )
    """
    emergency

    An unforeseen combination of circumstances or the resulting state that calls for immediate action.
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "definition": "Used to indicate that a service is to be performed prior to a scheduled surgery.  When ordering a service and using the pre-op priority, a check is done to see the amount of time that must be allowed for performance of the service.  When the order is placed, a message can be generated indicating the time needed for the service so that it is not ordered in conflict with a scheduled operation.",
            "display": "preop",
        }
    )
    """
    preop

    Used to indicate that a service is to be performed prior to a scheduled surgery.  When ordering a service and using the pre-op priority, a check is done to see the amount of time that must be allowed for performance of the service.  When the order is placed, a message can be generated indicating the time needed for the service so that it is not ordered in conflict with a scheduled operation.
    """

    prn = CodeSystemConcept(
        {
            "code": "PRN",
            "definition": 'An "as needed" order should be accompanied by a description of what constitutes a need. This description is represented by an observation service predicate as a precondition.',
            "display": "as needed",
        }
    )
    """
    as needed

    An "as needed" order should be accompanied by a description of what constitutes a need. This description is represented by an observation service predicate as a precondition.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Routine service, do at usual work hours.",
            "display": "routine",
        }
    )
    """
    routine

    Routine service, do at usual work hours.
    """

    rr = CodeSystemConcept(
        {
            "code": "RR",
            "definition": "A report should be prepared and sent as quickly as possible.",
            "display": "rush reporting",
        }
    )
    """
    rush reporting

    A report should be prepared and sent as quickly as possible.
    """

    s = CodeSystemConcept(
        {
            "code": "S",
            "definition": "With highest priority (e.g., emergency).",
            "display": "stat",
        }
    )
    """
    stat

    With highest priority (e.g., emergency).
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "It is critical to come as close as possible to the requested time (e.g., for a through antimicrobial level).",
            "display": "timing critical",
        }
    )
    """
    timing critical

    It is critical to come as close as possible to the requested time (e.g., for a through antimicrobial level).
    """

    ud = CodeSystemConcept(
        {
            "code": "UD",
            "definition": "Drug is to be used as directed by the prescriber.",
            "display": "use as directed",
        }
    )
    """
    use as directed

    Drug is to be used as directed by the prescriber.
    """

    ur = CodeSystemConcept(
        {"code": "UR", "definition": "Calls for prompt action.", "display": "urgent"}
    )
    """
    urgent

    Calls for prompt action.
    """

    class Meta:
        resource = _resource
