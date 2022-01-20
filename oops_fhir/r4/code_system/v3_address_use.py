from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AddressUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AddressUse:
    """
    v3 Code System AddressUse

     Codes that provide guidance around the circumstances in which a given
address should be used.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AddressUse
    """

    underscore_general_address_use = CodeSystemConcept(
        {
            "code": "_GeneralAddressUse",
            "concept": [
                {
                    "code": "BAD",
                    "definition": "Description: A flag indicating that the address is bad, in fact, useless.",
                    "display": "bad address",
                },
                {
                    "code": "CONF",
                    "definition": "Description: Indicates that the address is considered sensitive and should only be shared or published in accordance with organizational controls governing patient demographic information with increased sensitivity. Uses of Addresses.   Lloyd to supply more complete description.",
                    "display": "confidential address",
                },
                {
                    "code": "H",
                    "concept": [
                        {
                            "code": "HP",
                            "definition": "Description: The primary home, to reach a person after business hours.",
                            "display": "primary home",
                        },
                        {
                            "code": "HV",
                            "definition": "Description: A vacation home, to reach a person while on vacation.",
                            "display": "vacation home",
                        },
                    ],
                    "definition": "Description: A communication address at a home, attempted contacts for business purposes might intrude privacy and chances are one will contact family or other household members instead of the person one wishes to call. Typically used with urgent cases, or if no other contacts are available.",
                    "display": "home address",
                },
                {
                    "code": "OLD",
                    "definition": "This address is no longer in use.\r\n\n                        \n                           Usage Note: Address may also carry valid time ranges. This code is used to cover the situations where it is known that the address is no longer valid, but no particular time range for its use is known.",
                    "display": "no longer in use",
                },
                {
                    "code": "TMP",
                    "definition": "Description: A temporary address, may be good for visit or mailing. Note that an address history can provide more detailed information.",
                    "display": "temporary address",
                },
                {
                    "code": "WP",
                    "concept": [
                        {
                            "code": "DIR",
                            "definition": "Description: Indicates a work place address or telecommunication address that reaches the individual or organization directly without intermediaries. For phones, often referred to as a 'private line'.",
                            "display": "direct",
                        },
                        {
                            "code": "PUB",
                            "definition": "Description: Indicates a work place address or telecommunication address that is a 'standard' address which may reach a reception service, mail-room, or other intermediary prior to the target entity.",
                            "display": "public",
                        },
                    ],
                    "definition": "Description: An office address. First choice for business related contacts during business hours.",
                    "display": "work place",
                },
            ],
            "definition": "Description: Address uses that can apply to both postal and telecommunication addresses.",
            "display": "_GeneralAddressUse",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _GeneralAddressUse

    Description: Address uses that can apply to both postal and telecommunication addresses.
    """

    underscore_postal_address_use = CodeSystemConcept(
        {
            "code": "_PostalAddressUse",
            "concept": [
                {
                    "code": "PHYS",
                    "definition": "Description: Used primarily to visit an address.",
                    "display": "physical visit address",
                },
                {
                    "code": "PST",
                    "definition": "Description: Used to send mail.",
                    "display": "postal address",
                },
            ],
            "definition": "Description: Address uses that only apply to postal addresses, not telecommunication addresses.",
            "display": "_PostalAddressUse",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _PostalAddressUse

    Description: Address uses that only apply to postal addresses, not telecommunication addresses.
    """

    underscore_telecommunication_address_use = CodeSystemConcept(
        {
            "code": "_TelecommunicationAddressUse",
            "concept": [
                {
                    "code": "AS",
                    "definition": "Description: An automated answering machine used for less urgent cases and if the main purpose of contact is to leave a message or access an automated announcement.",
                    "display": "answering service",
                },
                {
                    "code": "EC",
                    "definition": "Description: A contact specifically designated to be used for emergencies. This is the first choice in emergencies, independent of any other use codes.",
                    "display": "emergency contact",
                },
                {
                    "code": "MC",
                    "definition": "Description: A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes, suitable for urgent matters, not the first choice for routine business.",
                    "display": "mobile contact)",
                },
                {
                    "code": "PG",
                    "definition": "Description: A paging device suitable to solicit a callback or to leave a very short message.",
                    "display": "pager",
                },
            ],
            "definition": "Description: Address uses that only apply to telecommunication addresses, not postal addresses.",
            "display": "_TelecommunicationAddressUse",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _TelecommunicationAddressUse

    Description: Address uses that only apply to telecommunication addresses, not postal addresses.
    """

    class Meta:
        resource = _resource
