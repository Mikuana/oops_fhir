from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_patient_importance import (
    v3PatientImportance as v3PatientImportance_,
)


__all__ = ["v3PatientImportance"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3PatientImportance(v3PatientImportance_):
    """
    v3 Code System PatientImportance

     Patient VIP code

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-PatientImportance
    """

    class Meta:
        resource = _resource
