from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActStatus:
    """
    v3 Code System ActStatus

     Codes representing the defined possible states of an Act, as defined by
the Act class state machine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActStatus
    """

    normal = CodeSystemConcept(
        {
            "code": "normal",
            "concept": [
                {
                    "code": "aborted",
                    "definition": "The Act has been terminated prior to the originally intended completion.",
                    "display": "aborted",
                },
                {
                    "code": "active",
                    "definition": "The Act can be performed or is being performed",
                    "display": "active",
                },
                {
                    "code": "cancelled",
                    "definition": "The Act has been abandoned before activation.",
                    "display": "cancelled",
                },
                {
                    "code": "completed",
                    "definition": "An Act that has terminated normally after all of its constituents have been performed.",
                    "display": "completed",
                },
                {
                    "code": "held",
                    "definition": "An Act that is still in the preparatory stages has been put aside.  No action can occur until the Act is released.",
                    "display": "held",
                },
                {
                    "code": "new",
                    "definition": "An Act that is in the preparatory stages and may not yet be acted upon",
                    "display": "new",
                },
                {
                    "code": "suspended",
                    "definition": "An Act that has been activated (actions could or have been performed against it), but has been temporarily disabled.  No further action should be taken against it until it is released",
                    "display": "suspended",
                },
            ],
            "definition": 'Encompasses the expected states of an Act, but excludes "nullified" and "obsolete" which represent unusual terminal states for the life-cycle.',
            "display": "normal",
        }
    )
    """
    normal

    Encompasses the expected states of an Act, but excludes "nullified" and "obsolete" which represent unusual terminal states for the life-cycle.
    """

    nullified = CodeSystemConcept(
        {
            "code": "nullified",
            "definition": "This Act instance was created in error and has been 'removed' and is treated as though it never existed.  A record is retained for audit purposes only.",
            "display": "nullified",
        }
    )
    """
    nullified

    This Act instance was created in error and has been 'removed' and is treated as though it never existed.  A record is retained for audit purposes only.
    """

    obsolete = CodeSystemConcept(
        {
            "code": "obsolete",
            "definition": "This Act instance has been replaced by a new instance.",
            "display": "obsolete",
        }
    )
    """
    obsolete

    This Act instance has been replaced by a new instance.
    """

    class Meta:
        resource = _resource
