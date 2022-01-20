from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.request_intent import RequestIntent as RequestIntent_


__all__ = ["RequestIntent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RequestIntent(RequestIntent_):
    """
    RequestIntent

    Codes indicating the degree of authority/intentionality associated with
a request.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/request-intent
    """

    class Meta:
        resource = _resource
