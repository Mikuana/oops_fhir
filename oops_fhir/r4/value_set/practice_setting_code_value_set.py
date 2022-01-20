from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["PracticeSettingCodeValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PracticeSettingCodeValueSet(ValueSet):
    """
    Practice Setting Code Value Set

    This is the code representing the clinical specialty of the clinician or
provider who interacted with, treated, or provided a service to/for the
patient. The value set used for clinical specialty has been limited by
HITSP to the value set reproduced from HITSP C80 Table 2-149 Clinical
Specialty Value Set Definition.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/c80-practice-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
