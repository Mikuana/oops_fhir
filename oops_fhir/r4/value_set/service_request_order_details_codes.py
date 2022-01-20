from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ServiceRequestOrderDetailsCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ServiceRequestOrderDetailsCodes(ValueSet):
    """
    Service Request Order Details Codes

    An example value set of Codified order entry details concepts.  These
concepts only make sense in the context of what is being ordered.  This
example is for a patient ventilation order

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/servicerequest-orderdetail
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
