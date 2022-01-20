from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_coding_rationale import (
    v3CodingRationale as v3CodingRationale_,
)


__all__ = ["v3CodingRationale"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3CodingRationale(v3CodingRationale_):
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

    http://terminology.hl7.org/ValueSet/v3-CodingRationale
    """

    class Meta:
        resource = _resource
