from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AcknowledgementDetailCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementDetailCode:
    """
    v3 Code System AcknowledgementDetailCode

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode
    """

    underscore_acknowledgement_detail_not_supported_code = CodeSystemConcept(
        {
            "code": "_AcknowledgementDetailNotSupportedCode",
            "concept": [
                {
                    "code": "NS200",
                    "definition": "The interaction (or: this version of the interaction) is not supported.",
                    "display": "Unsupported interaction",
                },
                {
                    "code": "NS202",
                    "definition": "The Processing ID is not supported.",
                    "display": "Unsupported processing id",
                },
                {
                    "code": "NS203",
                    "definition": "The Version ID is not supported.",
                    "display": "Unsupported version id",
                },
                {
                    "code": "NS250",
                    "definition": "The processing mode is not supported.",
                    "display": "Unsupported processing Mode",
                },
                {
                    "code": "NS260",
                    "definition": "The Device.id of the sender is unknown.",
                    "display": "Unknown sender",
                },
                {
                    "code": "NS261",
                    "definition": "The receiver requires information in the attentionLine classes for routing purposes.",
                    "display": "Unrecognized attentionline",
                },
            ],
            "definition": "Refelects rejections because elements of the communication are not supported in the current context.",
            "display": "AcknowledgementDetailNotSupportedCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AcknowledgementDetailNotSupportedCode

    Refelects rejections because elements of the communication are not supported in the current context.
    """

    interr = CodeSystemConcept(
        {
            "code": "INTERR",
            "definition": "An internal software component (database, application, queue mechanism, etc.) has failed, leading to inability to process the message.",
            "display": "Internal system error",
        }
    )
    """
    Internal system error

    An internal software component (database, application, queue mechanism, etc.) has failed, leading to inability to process the message.
    """

    nostore = CodeSystemConcept(
        {
            "code": "NOSTORE",
            "definition": "Rejection: The message can't be stored by the receiver due to an unspecified internal application issue. The message was neither processed nor stored by the receiving application.",
            "display": "No storage space for message.",
        }
    )
    """
    No storage space for message.

    Rejection: The message can't be stored by the receiver due to an unspecified internal application issue. The message was neither processed nor stored by the receiving application.
    """

    rtedest = CodeSystemConcept(
        {
            "code": "RTEDEST",
            "definition": "Error: The destination of this message is known to the receiving application. Messages have been successfully routed to that destination in the past. The link to the destination application or an intermediate application is unavailable.",
            "display": "Message routing error, destination unreachable.",
        }
    )
    """
    Message routing error, destination unreachable.

    Error: The destination of this message is known to the receiving application. Messages have been successfully routed to that destination in the past. The link to the destination application or an intermediate application is unavailable.
    """

    rtudest = CodeSystemConcept(
        {
            "code": "RTUDEST",
            "definition": "The destination of this message is unknown to the receiving application. The receiving application in the message does not match the application which received the message. The message was neither routed, processed nor stored by the receiving application.",
            "display": "Error: Message routing error, unknown destination.",
        }
    )
    """
    Error: Message routing error, unknown destination.

    The destination of this message is unknown to the receiving application. The receiving application in the message does not match the application which received the message. The message was neither routed, processed nor stored by the receiving application.
    """

    rtwdest = CodeSystemConcept(
        {
            "code": "RTWDEST",
            "definition": "Warning: The destination of this message is known to the receiving application. Messages have been successfully routed to that destination in the past. The link to the destination application or an intermediate application is (temporarily) unavailable. The receiving application will forward the message as soon as the destination can be reached again.",
            "display": "Message routing warning, destination unreachable.",
        }
    )
    """
    Message routing warning, destination unreachable.

    Warning: The destination of this message is known to the receiving application. Messages have been successfully routed to that destination in the past. The link to the destination application or an intermediate application is (temporarily) unavailable. The receiving application will forward the message as soon as the destination can be reached again.
    """

    syn = CodeSystemConcept(
        {
            "code": "SYN",
            "concept": [
                {
                    "code": "SYN102",
                    "definition": 'The attribute contained data of the wrong data type, e.g. a numeric attribute contained "FOO".',
                    "display": "Data type error",
                },
                {
                    "code": "SYN105",
                    "concept": [
                        {
                            "code": "SYN100",
                            "definition": "Required association missing in message; or the sequence of the classes is different than required by the standard or one of the conformance profiles identified in the message.",
                            "display": "Required association missing",
                        },
                        {
                            "code": "SYN101",
                            "definition": "A required attribute is missing in a class.",
                            "display": "Required attribute missing",
                        },
                        {
                            "code": "SYN114",
                            "definition": "Description: The number of repetitions of a group of association or attributes is less than the required minimum for the standard or of one of the conformance profiles or templates identified in the message.",
                            "display": "Insufficient repetitions",
                        },
                    ],
                    "definition": "Description: Required association or attribute missing in message; or the sequence of the classes is different than required by the standard or one of the conformance profiles identified in the message.",
                    "display": "Required element missing",
                },
                {
                    "code": "SYN106",
                    "concept": [
                        {
                            "code": "SYN103",
                            "definition": "An attribute value was compared against the corresponding code system, and no match was found.",
                            "display": "Value not found in code system",
                        },
                        {
                            "code": "SYN104",
                            "definition": "An attribute value referenced a code system that is not valid for an attribute constrained to CNE.",
                            "display": "Invalid code system in CNE",
                        },
                        {
                            "code": "SYN107",
                            "definition": "Description: A coded attribute is referencing a code that has been deprecated by the owning code system.",
                            "display": "Deprecated code",
                        },
                    ],
                    "definition": "Description: A coded attribute or datatype property violates one of the terminology constraints specified in the standard or one of the conformance profiles or templates declared by the instance.",
                    "display": "Terminology error",
                },
                {
                    "code": "SYN108",
                    "concept": [
                        {
                            "code": "SYN110",
                            "definition": "The number of repetitions of a (group of) association(s) exceeds the limits of the standard or of one of the conformance profiles identified in the message.",
                            "display": "Number of association repetitions exceeds limit",
                        },
                        {
                            "code": "SYN112",
                            "definition": "The number of repetitions of an attribute exceeds the limits of the standard or of one of the conformance profiles identified in the message.",
                            "display": "Number of attribute repetitions exceeds limit",
                        },
                    ],
                    "definition": "Description: The number of repetitions of a (group of) association(s) or attribute(s) exceeds the limits of the standard or of one of the conformance profiles or templates identified in the message.",
                    "display": "Number of repetitions exceeds limit",
                },
                {
                    "code": "SYN109",
                    "definition": "Description: An attribute or association identified as mandatory in a specification or declared conformance profile or template has been specified with a null flavor.",
                    "display": "Mandatory element with null value",
                },
                {
                    "code": "SYN111",
                    "definition": "Description: The value of an attribute or property differs from the fixed value asserted in the standard or one of the conformance profiles or templates declared in the message.",
                    "display": "Value does not match fixed value",
                },
                {
                    "code": "SYN113",
                    "definition": "Description: A formal constraint asserted in the standard or one of the conformance profiles or templates declared in the message has been violated.",
                    "display": "Formal constraint violation",
                },
            ],
            "definition": "Reflects errors in the syntax or structure of the communication.",
            "display": "Syntax error",
        }
    )
    """
    Syntax error

    Reflects errors in the syntax or structure of the communication.
    """

    class Meta:
        resource = _resource
