from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["VitalSigns"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class VitalSigns(ValueSet):
    """
    Vital Signs

    This value set indicates the allowed vital sign result types.   The
LOINC code for Vitals Signs panel (85353-1) is a grouping structure for
a set of vital signs and includes related links (with type=has-member)
to the Observations in this set (e.g. respiratory rate, heart rate, BP).
The Blood pressure panel (85354-9) is used to group the component
observations Systolic blood pressure (8480-6) and Diastolic blood
pressure (8462-4).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-vitalsignresult
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
