from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_marital_status import (
    v3MaritalStatus as v3MaritalStatus_,
)


__all__ = ["v3MaritalStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3MaritalStatus(v3MaritalStatus_):
    """
    v3 Code System MaritalStatus

     * * * No description supplied * * *  Open Issue:  The specific meanings
of these codes can vary somewhat by jurisdiction and implementation so
caution should be used when determining equivalency.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-MaritalStatus
    """

    class Meta:
        resource = _resource
