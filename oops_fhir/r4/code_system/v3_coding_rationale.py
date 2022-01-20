from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3CodingRationale"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3CodingRationale:
    """
    v3 Code System CodingRationale

     Identifies how to interpret the instance of the code, codeSystem value
in a set of translations.  Since HL7 (or a government body) may mandate
that codes from certain code systems be sent in conformant messages,
other synonyms that are sent in the translation set need to be
distinguished among the originally captured source, the HL7 specified
code, or some future role.  When this code is NULL, it indicates that
the translation is an undefined type.  When valued, this property must
contain one of the following values: SRC - Source (or original) code HL7
- HL7 Specified or Mandated SH - both HL7 mandated and the original code
(precoordination) There may be additional values added to this value set
as we work through the use of codes in messages and determine other Use
Cases requiring special interpretation of the translations.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-CodingRationale
    """

    o = CodeSystemConcept(
        {
            "code": "O",
            "definition": "Description: Originally produced code.",
            "display": "originally produced code",
        }
    )
    """
    originally produced code

    Description: Originally produced code.
    """

    or_ = CodeSystemConcept(
        {
            "code": "OR",
            "definition": "Originally produced code, required by the specification describing the use of the coded concept.",
            "display": "original and required",
        }
    )
    """
    original and required

    Originally produced code, required by the specification describing the use of the coded concept.
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "definition": "Description: Post-coded from free text source</description>",
            "display": "post-coded",
        }
    )
    """
    post-coded

    Description: Post-coded from free text source</description>
    """

    pr = CodeSystemConcept(
        {
            "code": "PR",
            "definition": "Post-coded from free text source, required by the specification describing the use of the coded concept.",
            "display": "post-coded and required",
        }
    )
    """
    post-coded and required

    Post-coded from free text source, required by the specification describing the use of the coded concept.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Description: Required standard code for HL7.",
            "display": "required",
        }
    )
    """
    required

    Description: Required standard code for HL7.
    """

    hl7 = CodeSystemConcept(
        {
            "code": "HL7",
            "definition": "HL7 Specified or Mandated",
            "display": "HL7 Specified or Mandated",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    HL7 Specified or Mandated

    HL7 Specified or Mandated
    """

    sh = CodeSystemConcept(
        {
            "code": "SH",
            "definition": "Both HL7 mandated and the original code (precoordination)",
            "display": "Both HL7 mandated and the original code",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Both HL7 mandated and the original code

    Both HL7 mandated and the original code (precoordination)
    """

    src = CodeSystemConcept(
        {
            "code": "SRC",
            "definition": "Source (or original) code",
            "display": "Source (or original) code",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Source (or original) code

    Source (or original) code
    """

    class Meta:
        resource = _resource
