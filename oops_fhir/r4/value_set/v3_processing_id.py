from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_processing_id import v3ProcessingID as v3ProcessingID_


__all__ = ["v3ProcessingID"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ProcessingID(v3ProcessingID_):
    """
    v3 Code System ProcessingID

     Codes used to specify whether a message is part of a production,
training, or debugging system.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ProcessingID
    """

    class Meta:
        resource = _resource
