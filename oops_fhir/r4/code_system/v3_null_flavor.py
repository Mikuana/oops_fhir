from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3NullFlavor"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3NullFlavor:
    """
    v3 Code System NullFlavor

     A collection of codes specifying why a valid value is not present.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-NullFlavor
    """

    ni = CodeSystemConcept(
        {
            "code": "NI",
            "concept": [
                {
                    "code": "INV",
                    "concept": [
                        {
                            "code": "DER",
                            "definition": "Description:An actual value may exist, but it must be derived from the provided information (usually an EXPR generic data type extension will be used to convey the derivation expressionexpression .",
                            "display": "derived",
                        },
                        {
                            "code": "OTH",
                            "concept": [
                                {
                                    "code": "NINF",
                                    "definition": "Negative infinity of numbers.",
                                    "display": "negative infinity",
                                },
                                {
                                    "code": "PINF",
                                    "definition": "Positive infinity of numbers.",
                                    "display": "positive infinity",
                                },
                            ],
                            "definition": "Description:The actual value is not a member of the set of permitted data values in the constrained value domain of a variable. (e.g., concept not provided by required code system).\r\n\n                        \n                           Usage Notes: This flavor and its specializations are most commonly used with the CD datatype and its flavors.  However, it may apply to *any* datatype where the constraints of the type are tighter than can be conveyed.  For example, a PQ that is for a true measured amount whose units are not supported in UCUM, a need to convey a REAL when the type has been constrained to INT, etc.\r\n\n                        With coded datatypes, this null flavor may only be used if the vocabulary binding has a coding strength of CNE.  By definition, all local codes and original text are part of the value set if the coding strength is CWE.",
                            "display": "other",
                        },
                        {
                            "code": "UNC",
                            "definition": "Description: The actual value has not yet been encoded within the approved value domain.\r\n\n                        \n                           Example: Original text or a local code has been specified but translation or encoding to the approved value set has not yet occurred due to limitations of the sending system.  Original text has been captured for a PQ, but not attempt has been made to split the value and unit or to encode the unit in UCUM.\r\n\n                        \n                           Usage Notes: If it is known that it is not possible to encode the concept, OTH should be used instead.  However, use of UNC does not necessarily guarantee the concept will be encodable, only that encoding has not been attempted.\r\n\n                        Data type properties such as original text and translations may be present when this null flavor is included.",
                            "display": "un-encoded",
                        },
                    ],
                    "definition": "Description:The value as represented in the instance is not a member of the set of permitted data values in the constrained value domain of a variable.",
                    "display": "invalid",
                },
                {
                    "code": "MSK",
                    "definition": "There is information on this item available but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information.\r\n\n                        Note: using this null flavor does provide information that may be a breach of confidentiality, even though no detail data is provided.  Its primary purpose is for those circumstances where it is necessary to inform the receiver that the information does exist without providing any detail.",
                    "display": "masked",
                },
                {
                    "code": "NA",
                    "definition": "Known to have no proper value (e.g., last menstrual period for a male).",
                    "display": "not applicable",
                },
                {
                    "code": "UNK",
                    "concept": [
                        {
                            "code": "ASKU",
                            "concept": [
                                {
                                    "code": "NAV",
                                    "definition": "Information is not available at this time but it is expected that it will be available later.",
                                    "display": "temporarily unavailable",
                                }
                            ],
                            "definition": "Information was sought but not found (e.g., patient was asked but didn't know)",
                            "display": "asked but unknown",
                        },
                        {
                            "code": "NASK",
                            "definition": "This information has not been sought (e.g., patient was not asked)",
                            "display": "not asked",
                        },
                        {
                            "code": "NAVU",
                            "definition": "Information is not available at this time (with no expectation regarding whether it will or will not be available in the future).",
                            "display": "Not available",
                            "property": [{"code": "child", "valueCode": "NAV"}],
                        },
                        {
                            "code": "QS",
                            "definition": "Description:The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material. e.g. 'Add 10mg of ingredient X, 50mg of ingredient Y, and sufficient quantity of water to 100mL.' The null flavor would be used to express the quantity of water.",
                            "display": "Sufficient Quantity",
                        },
                        {
                            "code": "TRC",
                            "definition": "The content is greater than zero, but too small to be quantified.",
                            "display": "trace",
                        },
                    ],
                    "definition": 'Description:A proper value is applicable, but not known.\r\n\n                        \n                           Usage Notes: This means the actual value is not known.  If the only thing that is unknown is how to properly express the value in the necessary constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used.  No properties should be included for a datatype with this property unless:\r\n\n                        \n                           Those properties themselves directly translate to a semantic of "unknown".  (E.g. a local code sent as a translation that conveys \'unknown\')\n                           Those properties further qualify the nature of what is unknown.  (E.g. specifying a use code of "H" and a URL prefix of "tel:" to convey that it is the home phone number that is unknown.)',
                    "display": "unknown",
                },
            ],
            "definition": "Description:The value is exceptional (missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value.",
            "display": "NoInformation",
        }
    )
    """
    NoInformation

    Description:The value is exceptional (missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value.
    """

    np = CodeSystemConcept(
        {
            "code": "NP",
            "definition": "Value is not present in a message.  This is only defined in messages, never in application data!  All values not present in the message must be replaced by the applicable default, or no-information (NI) as the default of all defaults.",
            "display": "not present",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    not present

    Value is not present in a message.  This is only defined in messages, never in application data!  All values not present in the message must be replaced by the applicable default, or no-information (NI) as the default of all defaults.
    """

    class Meta:
        resource = _resource
