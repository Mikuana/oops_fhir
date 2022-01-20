from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.httpverb import HTTPVerb as HTTPVerb_


__all__ = ["HTTPVerb"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HTTPVerb(HTTPVerb_):
    """
    HTTPVerb

    HTTP verbs (in the HTTP command line). See [HTTP
rfc](https://tools.ietf.org/html/rfc7231) for details.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/http-verb
    """

    class Meta:
        resource = _resource
