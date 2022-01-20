from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Charset"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Charset:
    """
    v3 Code System Charset

     Internet Assigned Numbers Authority (IANA) Charset Types

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Charset
    """

    ebcdic = CodeSystemConcept(
        {
            "code": "EBCDIC",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "EBCDIC",
        }
    )
    """
    EBCDIC

    HL7 is indifferent to the use of this Charset.
    """

    iso_10646_ucs_2 = CodeSystemConcept(
        {
            "code": "ISO-10646-UCS-2",
            "definition": "Deprecated for HL7 use.",
            "display": "ISO-10646-UCS-2",
        }
    )
    """
    ISO-10646-UCS-2

    Deprecated for HL7 use.
    """

    iso_10646_ucs_4 = CodeSystemConcept(
        {
            "code": "ISO-10646-UCS-4",
            "definition": "Deprecated for HL7 use.",
            "display": "ISO-10646-UCS-4",
        }
    )
    """
    ISO-10646-UCS-4

    Deprecated for HL7 use.
    """

    iso_8859_1 = CodeSystemConcept(
        {
            "code": "ISO-8859-1",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "ISO-8859-1",
        }
    )
    """
    ISO-8859-1

    HL7 is indifferent to the use of this Charset.
    """

    iso_8859_2 = CodeSystemConcept(
        {
            "code": "ISO-8859-2",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "ISO-8859-2",
        }
    )
    """
    ISO-8859-2

    HL7 is indifferent to the use of this Charset.
    """

    iso_8859_5 = CodeSystemConcept(
        {
            "code": "ISO-8859-5",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "ISO-8859-5",
        }
    )
    """
    ISO-8859-5

    HL7 is indifferent to the use of this Charset.
    """

    jis_2022_jp = CodeSystemConcept(
        {
            "code": "JIS-2022-JP",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "JIS-2022-JP",
        }
    )
    """
    JIS-2022-JP

    HL7 is indifferent to the use of this Charset.
    """

    us_ascii = CodeSystemConcept(
        {
            "code": "US-ASCII",
            "definition": "Required for HL7 use.",
            "display": "US-ASCII",
        }
    )
    """
    US-ASCII

    Required for HL7 use.
    """

    utf_7 = CodeSystemConcept(
        {
            "code": "UTF-7",
            "definition": "HL7 is indifferent to the use of this Charset.",
            "display": "UTF-7",
        }
    )
    """
    UTF-7

    HL7 is indifferent to the use of this Charset.
    """

    utf_8 = CodeSystemConcept(
        {
            "code": "UTF-8",
            "definition": "Required for Unicode support.",
            "display": "UTF-8",
        }
    )
    """
    UTF-8

    Required for Unicode support.
    """

    class Meta:
        resource = _resource
